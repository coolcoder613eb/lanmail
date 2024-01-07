class Client():
    def __init__(self, rfile, wfile): # Takes a file rather than a socket so other backends can be implemented, like serial.
        self.rfile=rfile
        self.wfile=wfile
        while True:
            line=rfile.readline()
            print(line)
    def waitfor(self,text):
        while True:
            line=rfile.readline().strip()
            print(line)
            if line.startswith(text):
                return line