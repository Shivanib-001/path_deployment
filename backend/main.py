import time
import json
import subprocess
from flask import Flask, Response, render_template

from gnss_read import GNSSData 


app = Flask(__name__)

data_read = GNSSData("../data/gnss.buf")

def start_gnss_writer():
    try:
        subprocess.Popen(["../src/gnss"])
        print("Reading live location data.")
    except Exception as e:
        print(f"Failed to process live loc: {e}")

@app.route("/")
def root():
    return render_template("page1.html")

def event_stream():
    while True:
        try:
            data = data_read.last_data()
            if data:
                yield f"data: {json.dumps(data)}\n\n"
            else:
                yield "data: {}\n\n"
            time.sleep(0.5)
        except Exception as e:
            print(f"Error in stream: {e}")
            break



@app.route('/livelocation', methods=['GET'])
def livelocation():
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    start_gnss_writer()
    time.sleep(1)
    app.run(host="0.0.0.0", port=3000, threaded=True)

