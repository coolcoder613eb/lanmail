import os
import json
from auth import getauth

PATH = "mail"
users = list(getauth().keys())


def addmsg(to, fro, msg, time):  # will return False if no such user found
    if to in users:
        msgs = readmsgs(to)
        msgs.append({"to": to, "from": fro, "text": msg, "time": time})
        writemsgs(to, msgs)
        return True
    else:
        return False


def readmsgs(user):
    with open(os.path.join(PATH, user + ".json"), "r") as f:
        return json.loads(f.read())


def writemsgs(user, msgs):
    with open(os.path.join(PATH, user + ".json"), "w") as f:
        f.write(json.dumps(msgs))
