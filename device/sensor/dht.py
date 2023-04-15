import statistics
from logger import logger
import Adafruit_DHT

from config_provider import config

import adafruit_dht
import board

class DHT:

    def __init__(self):
        self.gpio = config.get_config('GPIO/DHT/DATA_PIN')
        self.humidity = 0
        self.temperature = 0
        self.dhtDevice = adafruit_dht.DHT11(board.D4)

    def read_values(self):
        try:
            humidity_vals = []
            temperature_vals = []
            # get 10 values and calculate median. Lowers the chances of wrong data.
            for i in range(10):
                try:
                    humidity_vals.append(self.dhtDevice.humidity)
                    temperature_vals.append(self.dhtDevice.temperature)
                except RuntimeError as error:
                    # Errors happen fairly often, DHT's are hard to read, just keep going
                    logger.debug(str(error))
                    continue

            self.temperature = statistics.median(temperature_vals)
            self.humidity = statistics.median(humidity_vals)
            self.dhtDevice.exit()
        except Exception as error:
            self.dhtDevice.exit()
            logger.error(str(error))


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
