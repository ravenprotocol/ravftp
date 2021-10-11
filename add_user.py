import json
from _md5 import md5
from argparse import ArgumentParser
import shutil

from RavFTP.config import USERS_FILE_PATH


def add(username, password):
    users = None
    with open(USERS_FILE_PATH, 'r') as openfile:
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

        with open(USERS_FILE_PATH, "w") as f:
            json.dump(details, f)

        return {
            "username": username,
            "password": password
        }
    else:
        user = [user for user in users if user['username'] == username][0]
        return user


if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument("--username", type=str, default=None, help="Enter username")
    argparser.add_argument("--password", type=str, default=None, help="Enter password")

    args = argparser.parse_args()

    add(args.username, args.password)
