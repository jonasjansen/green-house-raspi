import json

from api.zigbee import zigbee
from config_provider import config


class ZigbeeBase:
    device_id = 0

    def get_state(self):
        try:
            response = zigbee.get_state(self.device_id)
            response_json = json.loads(response.content)

            if "state" in response_json and "on" in response_json["state"]:
                return bool(response_json["state"]["on"])

        except Exception as e:
            print(e)

        return False

    def turn_on(self):
        try:
            result = zigbee.set_state(self.device_id, json.dumps({"on": True}))
        except Exception as e:
            print("Could not turn on Zigbee device", self.device_id, ":", e)

    def turn_off(self):
        try:
            result = zigbee.set_state(self.device_id, json.dumps({"on": False}))
        except Exception as e:
            print(e)
