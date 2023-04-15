import statistics
from time import sleep

import Adafruit_DHT
import adafruit_dht

from config_provider import config
from logger import logger


class DHT:

    def __init__(self):
        self.gpio = config.get_config('GPIO/DHT/DATA_PIN')
        self.humidity = 0
        self.temperature = 0
        self.dhtDevice = adafruit_dht.DHT11(self.gpio)

    def read_values(self):
        try:
            humidity_vals = []
            temperature_vals = []
            # get 10 values and calculate median. Lowers the chances of wrong data.
            for i in range(3):
                try:
                    humidity, temperature = Adafruit_DHT.read_retry(11, self.gpio)

                    # the new method returns "None" very often. Therefore, it is not used here.
                    # humidity = self.dhtDevice.humidity
                    # temperature = self.dhtDevice.temperature
                    humidity_vals.append(humidity)
                    temperature_vals.append(temperature)

                    sleep(0.1)
                except RuntimeError as error:
                    # Errors happen fairly often, DHT's are hard to read, just keep going
                    logger.debug(str(error))
                    sleep(0.1)
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
