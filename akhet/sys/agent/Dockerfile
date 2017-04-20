FROM akhet/sys/base:latest

RUN pip install docker

ADD /opt/akhet-agent/ /opt/akhet-agent/
WORKDIR /opt/akhet-agent/
ENTRYPOINT python3 -u /opt/akhet-agent/app.py
