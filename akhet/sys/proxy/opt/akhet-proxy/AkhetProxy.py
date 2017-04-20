import json
import requests
import urllib.parse

class AkhetProxy(object):

    def __init__(self, akhet_api_url, akhet_hostname):
        super(AkhetProxy, self).__init__()
        self.akhet_api_url, akhet_hostname = akhet_api_url, akhet_hostname

        self.me = self.search_proxy(akhet_hostname)
        if self.me == None:
            payload = {}
            payload['hostname'] = akhet_hostname
            payload['status'] = "online"
            reply = requests.post(self.akhet_api_url+"/api/v1/proxy", json=payload)
            if reply.status_code != 201:
                raise ValueError("Reply status code: {}".format(reply.status_code))
            self.me = self.search_proxy(akhet_hostname)

    def search_proxy(self, akhet_hostname):
        payload = {}
        payload['hostname'] = akhet_hostname
        url = self.akhet_api_url+"/api/v1/proxy?{}".format(
            urllib.parse.urlencode({"where":json.dumps(payload)})
        )
        reply = requests.get(url)
        _items= reply.json()['_items']
        if len(_items) == 0:
            return None
        else:
            return _items[0]

    def get_hostname(self):
        return self.me['hostname']

    def poll(self):
        if self.me == None:
            raise ValueError("Wrong using of this object")
        else:
            url = self.akhet_api_url+"/api/v1/proxy/{}".format(self.me['_id'])
            self.me = requests.get(url).json()

    def me_is_online(self):
        if 'status' in self.me:
            return self.me['status'] == "online"
        return False
