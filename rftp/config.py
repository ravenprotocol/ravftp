import os
from os.path import expanduser
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = expanduser("~")

USERS_FILE_PATH = os.path.join(PROJECT_DIR, "users.json")
USER_TABLE_FILE_PATH = os.path.join(PROJECT_DIR, "user_table.json")
FILES_DIR = os.path.join(BASE_DIR, os.environ.get("FILES_DIR"), "files")

MASQUERADE_ADDRESS = os.environ.get("MASQUERADE_ADDRESS")
PASSIVE_PORTS = range(60000, 65535)
