from eve import Eve
from eve.auth import BasicAuth

import yaml

import fcntl
import signal
import os

class MyBasicAuth(BasicAuth):

    def __init__(self):
        super(MyBasicAuth, self).__init__()
        self.credentials = None

    def check_auth(self, username, password, allowed_roles, resource, method):
        print("{} {} {} {} {}".format(username,password,allowed_roles,resource,method))
        if self.credentials == None:
            filename = '/etc/akhet-api.yml'
            stream = open(filename)
            config = yaml.load(stream)
            self.credentials = config['credentials']
            stream.close()

        for credential in self.credentials['clients']:
            if credential['username'] == username and \
                credential['password'] == password:
                return True

        if resource == 'instance' or resource == 'agent':
            for credential in self.credentials['agents']:
                if credential['username'] == username and \
                    credential['password'] == password:
                    return True
        if resource == 'instance' or resource == 'proxy':
            for credential in self.credentials['proxies']:
                if credential['username'] == username and \
                    credential['password'] == password:
                    return True
        return False

if __name__ == '__main__':
    app = Eve(auth=MyBasicAuth)
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9020)
