from flask import Flask, request
import os
import threading
import globals as g
from helpers import restart_ftp_server
import warnings 

warnings.filterwarnings("ignore")

app = Flask(__name__)

def thread_function_add_user():#username, password):
    # g.ftp_server.authorizer.add_user(username, password, os.path.join(g.ftp_server.files_dir, username), perm='elradfmw')
    g.ftp_server.handler = g.ftp_server.initialize_handler()
    g.ftp_server.authorizer = g.ftp_server.handler.authorizer

@app.route('/add_user', methods = ['GET'])
def add_user():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    print("Flask Add user: ", username, password)
    thread_add_user = threading.Thread(target=thread_function_add_user)#, args=(username, password))
    thread_add_user.start()
    return 'User added successfully', 200
  
if __name__ == '__main__':

    thread_start_ftp_server = threading.Thread(target=restart_ftp_server)
    thread_start_ftp_server.start()

    app.run(port=5000, debug=False)
