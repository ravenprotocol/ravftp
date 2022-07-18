import os
from os.path import expanduser

FILES_DIR = os.environ.get("FILES_DIR")
USERS_FILE_PATH = os.environ.get("USERS_FILE_PATH")
USER_TABLE_FILE_PATH = os.environ.get("USER_TABLE_FILE_PATH")

BASE_DIR = os.path.join(expanduser("~"), "ravenverse/ravftp")
RAVFTP_LOG_FILE = os.path.join(BASE_DIR, "ravftp.log")

MASQUERADE_ADDRESS = os.environ.get("MASQUERADE_ADDRESS")
PASSIVE_PORTS = range(60000, 65535)
