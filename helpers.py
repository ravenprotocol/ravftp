import os
import signal
import time
from subprocess import Popen, PIPE

import globals as g
from rftp import FTP_Server


def start_server():
    g.ftp_server = FTP_Server(os.environ.get("FTP_SERVER_HOST"), os.environ.get("FTP_SERVER_PORT"))
    g.ftp_server.run()


def stop_server():
    port = 21
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:
        data = [x for x in process.split(" ") if x != '']
        if (len(data) <= 1):
            continue

        os.kill(int(data[1]), signal.SIGKILL)

    time.sleep(2)


def restart_ftp_server():
    stop_server()
    start_server()
