# serve_gzip_file

import gzip
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep

# python -m http.server # :)

FPATH = "data/temp_sensor_data.csv.gz"
PORT = 8081
SLEEP = .001

GZIP_FILE = gzip.open(FPATH, "rt", encoding="utf-8")

# http://localhost:8081

class StreamHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def do_GET(self):
        print("starting")
        self.send_response(200)

        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store")
        #self.send_header('Transfer-Encoding', 'chunked')
        self.end_headers()

        print("sent headers")

        for line in GZIP_FILE:
            #print(line)
            self.wfile.write(line.encode("utf-8"))
            self.wfile.flush()
            sleep(SLEEP)


if __name__ == "__main__":
    print("initing", PORT)
    HTTPServer(
        ('127.0.0.1', PORT), StreamHandler
    ).serve_forever()