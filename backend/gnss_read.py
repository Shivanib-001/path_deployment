import os

class GNSSData:
    def __init__(self, filepath):
        self.filepath = filepath
        self._last_line_count = 0

    def last_data(self):
        if not os.path.exists(self.filepath):
            return None

        try:
            with open(self.filepath, 'r') as file:
                lines = file.readlines()
                current_line_count = len(lines)

                if current_line_count <= self._last_line_count:
                    return None

                self._last_line_count = current_line_count
                last_line = lines[-1].strip()
                
                #expected data : Lat:28.1234,Lon:77.2345

                if "Lat" in last_line and "Lon" in last_line:
                    parts = last_line.replace(" ", "").split(",")
                    lat = float(parts[0].split(":")[1])
                    lon = float(parts[1].split(":")[1])
                    return {"latitude": lat, "longitude": lon}

        except Exception as e:
            print(f"Error reading GPS data: {e}")

        return None

