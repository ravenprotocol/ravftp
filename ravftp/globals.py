from .logger import get_logger
from .utils import Singleton


@Singleton
class Globals(object):
    def __init__(self):
        self._ftp_server = None
        self._logger = get_logger()

    @property
    def ftp_server(self):
        return self._ftp_server

    @ftp_server.setter
    def ftp_server(self, ftp_server):
        self._ftp_server = ftp_server

    @property
    def logger(self):
        return self._logger

globals = Globals.Instance()
