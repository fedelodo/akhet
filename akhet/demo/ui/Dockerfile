FROM debian:8

ADD ./etc/apt/sources.list /etc/apt/sources.list

RUN apt-get update && apt-get dist-upgrade -y

RUN apt-get install -y git && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y logrotate && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y cron && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y anacron && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y apache2 && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y php5 && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y php5-curl && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN apt-get install -y php5-dev && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete

RUN apt-get install -y libyaml-dev && \
  rm -f /var/cache/apt/archives/*deb && \
  find /var/log/ -type f -delete
RUN pecl install yaml && \
  echo "extension=yaml.so" > /etc/php5/mods-available/yaml.ini && \
  cd /etc/php5/cli/conf.d && \
  ln -s ../../mods-available/yaml.ini 30-yaml.ini && \
  cd /etc/php5/apache2/conf.d/ && \
  ln -s ../../mods-available/yaml.ini 30-yaml.ini

RUN a2enmod ssl
RUN a2ensite default-ssl.conf

RUN rm -f /var/www/html/index.html

RUN cd /var/www/html/ && \
  git clone https://github.com/noVNC/noVNC && \
  cd noVNC && \
  git checkout v0.6.2 && \
  rm .git -Rf

ADD ./opt/init.sh /opt/init.sh
RUN chmod +x /opt/init.sh
ENTRYPOINT /opt/init.sh

ADD ./var/www/html/ /var/www/html/
