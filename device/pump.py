from base import ZigbeeBase
from config_provider import config


class Pump(ZigbeeBase):
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/PUMP')


pump = Pump()
