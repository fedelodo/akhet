FROM akhet/sys/base:latest

ADD ./opt/akhet-api/ /opt/akhet-api/
WORKDIR /opt/akhet-api/
ENTRYPOINT python3 -u /opt/akhet-api/app.py

EXPOSE 9020
