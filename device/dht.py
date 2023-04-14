import statistics

import Adafruit_DHT

from base import ZigbeeBase
from config_provider import config


# install via 'sudo pip install Adafruit-DHT'
# NOTE: Is deprecated. Might want to replace it with https://pypi.org/project/adafruit-circuitpython-dht/

class DHT(ZigbeeBase):

    def __init__(self):
        self.gpio = config.get_config('GPIO/DHT/DATA_PIN')
        self.humidity = 0
        self.temperature = 0

    def read_values(self):
        humidity_vals = []
        temperature_vals = []

        # get 10 values and calculate median. Lowers the chances of wrong data.
        for i in range(10):
            cur_humidity, cur_temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.gpio)
            humidity_vals.append(cur_humidity)
            temperature_vals.append(cur_temperature)

        self.temperature = statistics.median(temperature_vals)
        self.humidity = statistics.median(humidity_vals)

    def get_temperature(self):
        self.read_values()
        return self.temperature

    def get_humidity(self):
        self.read_values()
        return self.humidity

    def get_values(self):
        self.read_values()
        return self.humidity, self.temperature


dht = DHT()
