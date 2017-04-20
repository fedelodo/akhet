# -*- coding: utf-8 -*-
MONGO_HOST = 'db'
MONGO_PORT = 27017
MONGO_DBNAME = 'akhet'
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20
#IF_MATCH = False
SOFT_DELETE = True
API_VERSION = "api/v1"
VERSIONING = True
XML = False
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
DEBUG = True

DOMAIN = {
    'instance': {
        'item_title': 'instance',
        'schema': {
            'status': {
                'type': 'string',
                'allowed': [
                    "pending",
                    "assigned",
                    "created",
                    "ready",
                    "running",
                    "stopped",
                    "deleted",
                ],
                'default': "pending"
            },
            'image': {
                'type': 'string',
                'required': True
            },
            'user': {
                'type': 'dict',
                'schema': {
                    'username': {
                        'type': 'string',
                        'default': 'akhet'
                    },
                    'user_label': {
                        'type': 'string',
                        'default':'Akhet'
                    },
                    'user_id': {
                        'type': 'integer',
                        'default':1000
                    },
                },
                'default': {'username':'akhet','user_label':'Akhet','user_id':1000}
            },
            'groups': {
                'type': 'dict',
                'default': {'akhetgroup':1000}
            },
            'env': {
                'type': 'dict',
                'default': {}
            },
            'port_ws_vnc': {
                'type': 'integer',
                'default': -1
            },
            'ports': {
                'type': 'list',
                'default': []
            },
            'agent_hostname': {
                'type': 'string'
            },
            'proxies_hostnames': {
                'type': 'list',
                "default": []
            },
            'time_started': {
                'type': 'datetime'
            },
            'time_stoped': {
                'type': 'datetime'
            },
            'time_to_live': {
                'type': 'integer',
                'default': -1
            },
            'persistent': {
                'type': 'boolean',
                'default': False
            },
            'shared': {
                'type': 'boolean',
                'default': False
            },
            'privileged': {
                'type': 'boolean',
                'default': False
            },
            'vnc_password': {
                'type': 'string',
                'default': "00000000"
            },
            'screen_size': {
                'type': 'dict',
                'schema': {
                    'x': {
                        'type': 'integer'
                    },
                    'y': {
                        'type': 'integer'
                    },
                    'available': {
                        'type': 'list'
                    }
                },
                'default': {'x':-1,'y':-1,"available":[]}
            }
        }
    },
    'proxy': {
        'item_title': 'proxy',
        'schema': {
            'hostname': {
                'type': 'string',
                'required': True
            },
            'status': {
                'type': 'string',
                'allowed': ["online", "maintenance", "decommissioning", "offline"],
                'default': "maintenance"
            }
        }
    },
    'agent': {
        'item_title': 'agent',
        'schema': {
            'hostname': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'status': {
                'type': 'string',
                'allowed': ["online", "maintenance", "decommissioning", "offline"],
                'default': "maintenance"
            },
            'images': {
                'type': 'list',
            }
        }
    }
}
