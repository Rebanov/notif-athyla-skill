#!/user/bin/env python3
import time
from http.server import HTTPServer
from server import Server

HOST_NAME = 'localhost'
PORT_NUMBER = 8000

if __name__ == "__main__"
    httpd = HTTPServer((HOTS_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
       http.serve_forever()
    except keyboardInterrupt:
        pass
    http.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOTS_NAME, PORT_NUMBER))
