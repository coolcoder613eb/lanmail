import socketserver
import handleclient

class MailHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print(self.request)
        handleclient.Client(self.rfile,self.wfile)

def main():
    HOST, PORT = "0.0.0.0", 1865 # from sum(ord(x) for x in 'Simplified Lan Email') ;)
	
    with socketserver.TCPServer((HOST, PORT), MailHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()