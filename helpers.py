import os
import signal
from subprocess import Popen, PIPE

from rftp import FTP_Server


def start_server():
    ftp_server = FTP_Server("0.0.0.0", 21)
    ftp_server.run()


def stop_server():
    port = 21
    process = Popen(["lsof", "-i", ":{0}".format(port)], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    for process in str(stdout.decode("utf-8")).split("\n")[1:]:
        data = [x for x in process.split(" ") if x != '']
        if (len(data) <= 1):
            continue

        os.kill(int(data[1]), signal.SIGKILL)


def restart_ftp_server():
    stop_server()
    start_server()
