from config_provider import config
from pump import Pump


class PumpHumidity(Pump):
    def __init__(self):
        self.device_id = config.get_config('ZIGBEE/ID/PUMP')
        self.gpio_direction = config.get_config('GPIO/PUMP_HUMIDITY/DIRECTION')
        self.gpio_step = config.get_config('GPIO/PUMP_HUMIDITY/STEP')


pump_watering = PumpHumidity()
