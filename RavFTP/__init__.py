import json
import os
import sys
from hashlib import md5

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import BASE_DIR, USERS_FILE_PATH, USER_TABLE_FILE_PATH, FILES_DIR, MASQUERADE_ADDRESS, PASSIVE_PORTS


class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        # print(username, password, self.user_table)
        if sys.version_info >= (3, 0):
            password = password.encode('latin1')
        hash = md5(password).hexdigest()
        try:
            # print(hash, self.user_table[username]['pwd'])
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed


class FTP_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.base_dir = FILES_DIR
        self.handler = self.initialize_handler()
        self.ftp_server = FTPServer((self.host, self.port), self.handler)

    def get_users(self):
        with open(USERS_FILE_PATH, 'r') as f:
            details = json.load(f)
            users = details['users']
            return users

    def initialize_handler(self):
        authorizer = DummyMD5Authorizer()

        for user in self.get_users():
            if not authorizer.has_user(user['username']):
                os.makedirs(os.path.join(self.base_dir, user['username']), exist_ok=True)
                password = user['password']
                # if sys.version_info >= (3, 0):
                #     password = password.encode('latin1')
                # hash = md5(password).hexdigest()
                authorizer.add_user(user['username'], password,
                                    os.path.join(self.base_dir, user['username']), perm='elradfmw')

        print(authorizer.user_table)
        with open(USER_TABLE_FILE_PATH, "w") as outfile:
            json.dump(authorizer.user_table, outfile)

        handler = FTPHandler
        handler.authorizer = authorizer
        handler.permit_foreign_addresses = True
        handler.permit_privileged_ports = True
        handler.masquerade_address = MASQUERADE_ADDRESS
        handler.passive_ports = PASSIVE_PORTS
        return handler

    def run(self):
        self.ftp_server.serve_forever()
