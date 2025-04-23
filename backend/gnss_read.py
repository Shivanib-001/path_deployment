import os

class GNSSData:
    def __init__(self, filepath):
        self.filepath = filepath
        self._last_line = None

    def last_data(self):
        if not os.path.exists(self.filepath):
            return None

        try:
            with open(self.filepath, 'rb') as file:

                file.seek(0, os.SEEK_END)
                file_size = file.tell()
                block_size = 1024
                data = b''
                while file_size > 0:
                    seek_size = min(block_size, file_size)
                    file.seek(file_size - seek_size)
                    chunk = file.read(seek_size)
                    data = chunk + data
                    file_size -= seek_size
                    if b'\n' in chunk:
                        break

                lines = data.split(b'\n')
                last_line = lines[-1] if lines[-1] else lines[-2]
                last_line = last_line.decode().strip()

                self._last_line = last_line

                if "Lat" in last_line and "Lng" in last_line:
                    parts = last_line.split(":")
                    lat = float(parts[4].split(" ")[1])
                    lon = float(parts[5].split(" ")[1])
                    print(lat, lon)
                    return {"latitude": lat, "longitude": lon}

        except Exception as e:
            print(f"Error reading GPS data: {e}")

        return None
