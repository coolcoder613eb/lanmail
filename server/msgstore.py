import os
import json
from auth import getauth

PATH = "mail"
users = list(getauth().keys())


def addmsg(to, msg):  # will return False if no such user found
    if to in users:
        msgs = readmsgs(to)
        msgs.append(msg)
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
