# ravftp

Ravftp is a combination of flask and ftp server that facilitates file/data transfer among requesters and providers

#### Create a .env file

    touch .env

#### Set environment variables

    MASQUERADE_ADDRESS=127.0.0.1
    FLASK_SERVER_HOST=0.0.0.0
    FLASK_SERVER_PORT=5001
    FTP_SERVER_HOST=0.0.0.0
    FTP_SERVER_PORT=21
    FILES_DIR=ravenverse/ravftp

#### Start the flask server

    python app.py

Note: The Flask server will initialize and start the ftp server automatically. There is no need to start it separately.
