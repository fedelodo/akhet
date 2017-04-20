import json
import requests
import urllib.parse

class AkhetAgent(object):

    def __init__(self, akhet_api_url, akhet_hostname):
        super(AkhetAgent, self).__init__()
        self.akhet_api_url, akhet_hostname = akhet_api_url, akhet_hostname

        self.images_list = []

        self.me = self.search_agent(akhet_hostname)
        if self.me == None:
            payload = {}
            payload['hostname'] = akhet_hostname
            payload['status'] = "online"
            reply = requests.post(self.akhet_api_url+"/api/v1/agent", json=payload)
            if reply.status_code != 201:
                raise ValueError("Reply status code: {}".format(reply.status_code))
            self.me = self.search_agent(akhet_hostname)

    def search_agent(self, akhet_hostname):
        payload = {}
        payload['hostname'] = akhet_hostname
        url = self.akhet_api_url+"/api/v1/agent?{}".format(
            urllib.parse.urlencode({"where":json.dumps(payload)})
        )
        reply = requests.get(url)
        _items= reply.json()['_items']
        if len(_items) == 0:
            return None
        else:
            return _items[0]

    def set_images_list(self, images_list):
        if len(self.images_list) != len(images_list) or \
            not list(set(self.images_list) & set(images_list)):
            url = self.akhet_api_url+"/api/v1/agent/{}".format(self.me['_id'])
            reply = requests.patch(
                url=url,
                json={"images":images_list},
                headers={'If-Match': self.me['_etag']}
            )
            self.images_list = images_list

    def get_hostname(self):
        return self.me['hostname']

    def poll(self):
        if self.me == None:
            raise ValueError("Wrong using of this object")
        else:
            url = self.akhet_api_url+"/api/v1/agent/{}".format(self.me['_id'])
            self.me = requests.get(url).json()

    def me_is_online(self):
        if 'status' in self.me:
            return self.me['status'] == "online"
        return False
