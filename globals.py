from utils import Singleton

@Singleton
class Globals(object):
    def __init__(self):
        self._ftp_server = None

    @property
    def ftp_server(self):
        return self._ftp_server

    @ftp_server.setter
    def ftp_server(self, ftp_server):
        self._ftp_server = ftp_server

globals = Globals.Instance()
