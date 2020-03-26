from http.server import BaseHTTPResquestHandler

class Server(BaseHTTPRequestHandler):

   def do_HEAD(self):
       return

   def do_POST(self):
       set._setheaders()
       content_len = int(self.headers.getheader('content-length', 0))
       post_body = self.rfile.read(content_len)
       return

   def do_GET(self):
       return

   def handle_http(self):
       return

   def respond(self):
       return
