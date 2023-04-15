import statistics
from time import sleep

import adafruit_ads1x15.ads1115 as ADS
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn

from config_provider import config


class Moisture:

    def __init__(self):
        self.gpio = config.get_config('GPIO/MOISTURE/DATA_PIN')
        self.moisture = 0

        i2c = busio.I2C(board.SCL, board.SDA)
        # Create the ADC object using the I2C bus
        ads = ADS.ADS1115(i2c)
        # Create single-ended input on channels
        self.chan0 = AnalogIn(ads, ADS.P0)
        self.chan1 = AnalogIn(ads, ADS.P1)
        self.chan2 = AnalogIn(ads, ADS.P2)
        self.chan3 = AnalogIn(ads, ADS.P3)

    def get_moisture(self):
        self.read_moisture()
        return self.moisture

    def read_moisture(self):
        values = []
        for i in range(10):
            values.append(self.chan0.voltage)
            sleep(0.1)
        print(values)
        self.moisture = "{:>5.3f}".format(statistics.median(values))


moisture = Moisture()
