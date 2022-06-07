import os

from dotenv import load_dotenv

load_dotenv()

from ravftp import flask_server

if __name__ == '__main__':
    flask_server.start()
