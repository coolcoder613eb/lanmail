from auth import authenticate
import msgstore


class Client:
    def __init__(
        self, rfile, wfile
    ):  # Takes a file rather than a socket so other backends can be implemented, like serial.
        self.rfile = rfile
        self.wfile = wfile
        # Will loop until client is authenticated
        while True:
            user = self.waitfor("AUTH USER ")
            password = self.waitfor("AUTH PASSWD ")
            if authenticate(user, password):
                self.send_msg("AUTH ACCEPTED")
                self.user = user
                break
            else:
                self.send_msg("AUTH REJECTED")

        # TODO: check for new messages

        # Main loop
        while True:
            line = self.waitfor()
            tokens = line.split()
            if len(tokens) == 2:
                if tokens[0] == "SEND" and tokens[1].isdigit():
                    length = int(tokens[1])
                    msg = self.rfile.read(length).decode()
                    print(repr(msg))
                    tokens = self.waitfor().split()
                    if len(tokens) == 2:
                        if tokens[0] == "TO":
                            print(tokens[1])
                            if msgstore.addmsg(tokens[1], msg):
                                self.send_msg("SEND OK")
                            else:
                                self.send_msg("SEND FAILED")

    def send_msg(self, text):
        self.wfile.write(text.encode())

    def waitfor(self, text=""):
        while True:
            line = self.rfile.readline().decode().strip()
            print(line)
            if line.startswith(text):
                return line.removeprefix(text)
