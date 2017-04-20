#!/usr/bin/env python3
import time
import yaml
from pprint import pprint
import socket
import os
import os.path
import requests
import glob

from AkhetInstanceManager import AkhetInstanceManager
from AkhetInstance import AkhetInstance
from AkhetProxy import AkhetProxy

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config_stream = open("/etc/akhet-proxy.yml", "r")
config = yaml.load(config_stream)
config_stream.close()

akhet_api_base = str(config['api_protocol'])
akhet_api_base = akhet_api_base + "://"
akhet_api_base = akhet_api_base + str(config['api_username'])
akhet_api_base = akhet_api_base + ":"
akhet_api_base = akhet_api_base + str(config['api_password'])
akhet_api_base = akhet_api_base + "@"
akhet_api_base = akhet_api_base + str(config['api_host'])
akhet_api_base = akhet_api_base + ":"
akhet_api_base = akhet_api_base + str(config['api_port'])

this_hostname = socket.gethostname()
if 'this_hostname' in config:
    this_hostname = config['this_hostname']
if 'use_ip_as_hostname' in config and config['use_ip_as_hostname']:
    this_hostname = socket.gethostbyname(this_hostname)
akhet_proxy = AkhetProxy(akhet_api_base, this_hostname)


logger.info("Getting Akhet instance manager with {} API host...".format(akhet_api_base))
akhet_instance_manager = AkhetInstanceManager(akhet_api_base)

logger.info("run...")
while True:
    akhet_proxy.poll()
    if akhet_proxy.me_is_online():
        files = []
        for instance_id in akhet_instance_manager.get_list_running_isntances():
            instance = AkhetInstance(akhet_api_base,instance_id)
            instance.poll()

            file_name = "{}portvnc@{}@{}".format(
                os.environ['AKHET_RUN_DIR'],
                instance.get_agent_hostname(),
                instance.get_port_ws_vnc()
            )
            files.append(file_name)

            if not os.path.isfile(file_name):
                fhandle = open(file_name, 'a')
                fhandle.close()

                instance.add_proxy_hostname(this_hostname)

        all_files = glob.glob("{}*".format(os.environ['AKHET_RUN_DIR']))
        for file_name in all_files:
            if not file_name in files:
                os.unlink(file_name)

    else:
        print("NOT ONLINE")
    time.sleep(1)
