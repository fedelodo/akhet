#!/bin/bash

export AKHET_CERTS_DIR=${AKHET_CONF_DIR}ssl/
export AKHET_CERT_CRT_FILE=${AKHET_CERTS_DIR}akhet.crt
export AKHET_CERT_KEY_FILE=${AKHET_CERTS_DIR}akhet.key
export AKHET_API_IP_WHITELIST_FILE=${AKHET_CONF_DIR}ip-whitelist
export AKHET_API_HOSTS_LIST_FILE=${AKHET_CONF_DIR}api-hosts

if test ! -d $AKHET_RUN_DIR ; then
  mkdir $AKHET_RUN_DIR
fi
if test ! -d $AKHET_CERTS_DIR ; then
  mkdir $AKHET_CERTS_DIR
fi
if test ! -f $AKHET_CERT_KEY_FILE ; then
  if test ! -f $AKHET_CERT_CRT_FILE ; then
    echo "Making self signed certificate..."
    echo "THIS IS BAD"
    openssl req \
      -subj "/CN=localhost" \
      -new -newkey rsa:2048 -days 365 \
      -nodes -x509 \
      -keyout $AKHET_CERT_KEY_FILE \
      -out $AKHET_CERT_CRT_FILE
  else
    echo "Found $AKHET_CERT_CRT_FILE but not $AKHET_CERT_KEY_FILE"
    exit 1
  fi
fi

cd

if test ! -f $AKHET_API_HOSTS_LIST_FILE
then
  if [ ! -z $API_PORT_9020_TCP_ADDR ]
  then
    {
      echo "http://"$API_PORT_9020_TCP_ADDR":9020"
    } &> $AKHET_API_HOSTS_LIST_FILE
  else
    echo "Missing API_PORT_9020_TCP"
    sleep 10
    exit 1
  fi
fi

if test ! -f $AKHET_API_IP_WHITELIST_FILE
then
  {
    echo "192.168.0.0/16"
    echo "172.16.0.0/12"
    echo "10.0.0.0/8"
    echo "127.0.0.0/8"
  } &> $AKHET_API_IP_WHITELIST_FILE
fi

/etc/init.d/dnsmasq start &> /dev/null
nginx -c /etc/nginx/nginx.conf
exec python3 -u /opt/akhet-proxy/app.py
