FROM        akhet/base/image-ubuntu-16-04:latest

RUN apt-get -y install gnome-shell && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get -y install gnome-terminal && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get -y install nautilus && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete

ADD ./gnome.conf /etc/supervisor/conf.d/
