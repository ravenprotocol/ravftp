from __future__ import annotations
from ravftp.logger import get_logger

logger = get_logger()


if __name__ == '__main__':
    from ravftp import flask_server
    flask_server.start()
