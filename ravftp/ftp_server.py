import grp
import json
import logging
import os
import sys
from hashlib import md5
from pwd import getpwnam

from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from .config import USERS_FILE_PATH, USER_TABLE_FILE_PATH, FILES_DIR, MASQUERADE_ADDRESS, PASSIVE_PORTS


class DummyMD5Authorizer(DummyAuthorizer):

    def validate_authentication(self, username, password, handler):
        if sys.version_info >= (3, 0):
            password = password.encode('latin1')
        hash = md5(password).hexdigest()
        try:
            if self.user_table[username]['pwd'] != hash:
                raise KeyError
        except KeyError:
            raise AuthenticationFailed


class FTP_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.files_dir = FILES_DIR
        self.handler = self.initialize_handler()
        self.ftp_server = FTPServer((self.host, self.port), self.handler)
        self.authorizer = self.handler.authorizer

    def get_users(self):
        with open(USERS_FILE_PATH, 'r') as f:
            details = json.load(f)
            users = details['users']
            return users

    def initialize_handler(self):
        authorizer = DummyMD5Authorizer()

        for user in self.get_users():
            if not authorizer.has_user(user['username']):
                os.makedirs(os.path.join(self.files_dir, user['username']), exist_ok=True)
                os.chown(os.path.join(self.files_dir, user['username']),  getpwnam('apple').pw_uid,
                         grp.getgrnam('apple').gr_gid)
                password = user['password']
                authorizer.add_user(user['username'], password,
                                    os.path.join(self.files_dir, user['username']), perm='elradfmw')

        import pprint
        print(pprint.pformat(authorizer.user_table))
        with open(USER_TABLE_FILE_PATH, "w") as outfile:
            json.dump(authorizer.user_table, outfile)

        handler = FTPHandler
        handler.authorizer = authorizer
        handler.permit_foreign_addresses = True
        handler.permit_privileged_ports = True
        handler.masquerade_address = MASQUERADE_ADDRESS
        handler.passive_ports = PASSIVE_PORTS
        logging.basicConfig(filename='log.txt', level=logging.DEBUG)
        print("Handler initiated")
        return handler

    def run(self):
        self.ftp_server.serve_forever()
