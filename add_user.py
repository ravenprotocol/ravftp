import json
from _md5 import md5
from argparse import ArgumentParser
import shutil


def add(username, password):
    users = None
    shutil.copyfile("users.json", "users-old.json")
    with open('users.json', 'r') as openfile:
        details = json.load(openfile)
        users = details['users']

    # Check user
    if len([user['username'] for user in users if user['username'] == username]) == 0:
        # Do not add user
        password = md5(password.encode("latin1")).hexdigest()
        users.append({
            "username": username,
            "password": password
        })

        details['users'] = users

        with open("users.json", "w") as f:
            json.dump(details, f)
    else:
        raise Exception("User already exists")


if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument("--username", type=str, default=None, help="Enter username")
    argparser.add_argument("--password", type=str, default=None, help="Enter password")

    args = argparser.parse_args()

    add(args.username, args.password)
