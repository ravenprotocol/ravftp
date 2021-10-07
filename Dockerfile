FROM python:3.7-alpine

COPY . /

RUN pip3 install -r requirements.txt

EXPOSE 21 20

ENTRYPOINT python3 start_federated_server.py