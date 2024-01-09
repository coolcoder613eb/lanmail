from auth import getauth, PATH
import os
import json
from sys import argv

MAIL = "mail"
user = argv[1]
password = argv[2]
if not os.path.isdir(MAIL):
    os.mkdir(MAIL)
mailusers = os.listdir(MAIL)
if user + ".json" not in mailusers:
    with open(os.path.join(MAIL, user + ".json"), "w") as f:
        f.write("[]")
auth = getauth()
if user not in auth:
    auth[user] = password
with open(PATH, "w") as f:
    f.write(json.dumps(auth))
