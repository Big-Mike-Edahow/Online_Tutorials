# server.py
# A simple Python HTTP Server

import http.server  # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", 8001), Handler) as httpd:
    print("Serving HTTP on port 8001...")
    httpd.serve_forever()

