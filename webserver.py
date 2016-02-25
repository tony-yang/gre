import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 8080

os.chdir(webdir)
server_address = ('', port)
server_object = HTTPServer(server_address, CGIHTTPRequestHandler)
server_object.serve_forever()
