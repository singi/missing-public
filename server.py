#!/usr/bin/python3

import os
import sys
import signal
from http.server import BaseHTTPRequestHandler,HTTPServer,ThreadingHTTPServer
sys.path.append( os.getcwd() + r"/domato/")
import generator

SERVER_PORT = 8282

def s2b(s):
	return str.encode(s)

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header('Content-Type', 'text/html')        
        self.end_headers()
        #get testcase
        generator.generate_samples("./testcase/testcase.html")        
        self.wfile.write(s2b(open("./testcase/testcase.html", "r").read()))
        return
        
    def log_message(self, format, *args):
        return

def signalHandler(sig, frame):
    print("[-] DASH WebServer Exited.")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signalHandler)
    server = ThreadingHTTPServer(('0.0.0.0', SERVER_PORT), requestHandler)
    print("[*] WebServer on " + str(SERVER_PORT))
    server.serve_forever()
    