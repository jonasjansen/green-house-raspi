import json

from api.zigbee import zigbee
from config_provider import config


class Light:
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/LIGHT')

    def get_state(self):
        result = zigbee.get_state(self.device_id)
        return result

    def turn_on(self):
        result = zigbee.set_state(self.device_id, json.dumps({"on": True}))

    def turn_off(self):
        result = zigbee.set_state(self.device_id, json.dumps({"on": False}))


light = Light()
