import json

from api.zigbee import zigbee
from config_provider import config


class Heater:
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/HEATER')

    def get_state(self):
        response = zigbee.get_state(self.device_id)
        response_json = json.loads(response.content)

        if "state" in response_json and "on" in response_json["state"]:
            return bool(response_json["state"]["on"])
        else:
            return False

    def turn_on(self):
        result = zigbee.set_state(self.device_id, json.dumps({"on": True}))

    def turn_off(self):
        result = zigbee.set_state(self.device_id, json.dumps({"on": False}))


heater = Heater()
