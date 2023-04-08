import json
import time

import requests

from config_provider import config


class Zigbee:
    api_url = ""
    api_key = ""

    def __init__(self):
        self.api_url = config.get_config('ZIGBEE/API_IP')
        self.api_key = config.get_config('ZIGBEE/API_KEY')

    def get_api_url(self):
        return ''.join(('http://', self.api_url, '/api/', self.api_key, '/lights/'))

    def get_state(self, device_id):
        request_url = ''.join((self.get_api_url(), str(device_id)))
        return requests.get(request_url)

    def set_state(self, device_id, payload):
        request_url = ''.join((self.get_api_url(), str(device_id), '/state/'))
        return requests.put(request_url, data=payload)


zigbee = Zigbee()
