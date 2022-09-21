FROM python:3.7-alpine

COPY . /

RUN pip3 install -r requirements.txt

EXPOSE 5000 21

RUN python3 run.py --action start &

ENTRYPOINT python3 app.py
