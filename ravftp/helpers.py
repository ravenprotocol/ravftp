from __future__ import annotations

import os
import signal
import time
from subprocess import PIPE
from subprocess import Popen

from .ftp_server import FTP_Server
from .globals import globals as g


def start_server():
    g.ftp_server = FTP_Server(os.environ.get(
        'FTP_SERVER_HOST'), os.environ.get('FTP_SERVER_PORT'))
    g.ftp_server.run()


def stop_server():
    port = 21
    process = Popen(['lsof', '-i', f':{port}'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode('utf-8')).split('\n')[1:]:
        data = [x for x in process.split(' ') if x != '']
        if (len(data) <= 1):
            continue

        os.kill(int(data[1]), signal.SIGKILL)

    time.sleep(2)


def restart_ftp_server():
    stop_server()
    start_server()
