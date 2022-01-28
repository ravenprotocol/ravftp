import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

USERS_FILE_PATH = os.path.join(BASE_DIR, "users.json")
USER_TABLE_FILE_PATH = os.path.join(BASE_DIR, "user_table.json")
FILES_DIR = os.path.join(str(Path.home()), "ravftp", "files")

MASQUERADE_ADDRESS = "54.201.212.222"
PASSIVE_PORTS = range(60000, 65535)
