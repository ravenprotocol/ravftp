import os
from argparse import ArgumentParser

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

if __name__ == '__main__':
    os.getcwd()

    files_dir = os.path.join(os.path.expanduser("~"), "ravenverse/ravftp/files")
    users_file_path = os.path.join(os.getcwd(), "users.json")
    user_table_file_path = os.path.join(os.getcwd(), "user_table.json")

    argparser = ArgumentParser()
    argparser.add_argument("-fh", "--flask_server_host", type=str,
                           help="Enter the host address of flask server to start", default="0.0.0.0")
    argparser.add_argument("-fp", "--flask_server_port", type=str, help="Enter the port of flask server",
                           default="5001")
    argparser.add_argument("-ffh", "--flask_ftp_host", type=str, help="Enter the host address of ftp server to start",
                           default="0.0.0.0")
    argparser.add_argument("-ffp", "--flask_ftp_port", type=str, help="Enter the port of ftp server", default="21")
    argparser.add_argument("-m", "--masquerade_address", type=str, help="Enter masquerade address", default="127.0.0.1")
    argparser.add_argument("-f", "--files_dir", type=str, help="Enter files directory to use", default=files_dir)
    argparser.add_argument("-uf", "--users_file", type=str, help="Enter path of users.json", default=users_file_path)
    argparser.add_argument("-utf", "--users_table_file", type=str, help="Enter path of user_table.json",
                           default=user_table_file_path)

    args = argparser.parse_args()

    os.environ["MASQUERADE_ADDRESS"] = args.masquerade_address
    os.environ["FLASK_SERVER_HOST"] = args.flask_server_host
    os.environ["FLASK_SERVER_PORT"] = args.flask_server_port
    os.environ["FTP_SERVER_HOST"] = args.flask_ftp_host
    os.environ["FTP_SERVER_PORT"] = args.flask_ftp_port
    os.environ["FILES_DIR"] = args.files_dir
    os.environ["USERS_FILE_PATH"] = args.users_file
    os.environ["USER_TABLE_FILE_PATH"] = args.users_table_file

    from ravftp import flask_server

    flask_server.start()
