import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><body>Hello, world !</body></html>')
        return
    
if __name__ == '__main__':
    print "Listening on port 8088:"
    server = BaseHTTPServer.HTTPServer(('',8088),MyHandler)
    server.serve_forever()