import json

PATH = "auth.json"


def getauth():
    with open(PATH, "r") as f:
        return json.loads(f.read())


def authenticate(user, password):
    db = getauth()
    print(db)
    if user in db:
        if password == db[user]:
            return True
    return False
