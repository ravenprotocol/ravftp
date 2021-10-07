import os

from RavFTP import FTP_Server

os.makedirs("collected_model", exist_ok=True)

ftp_server = FTP_Server("0.0.0.0", 21)
ftp_server.run()
