# Howto: https://joy-it.net/files/files/Produkte/SEN-Moisture/SEN-Moisture-Manual.pdf

from time import sleep
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# Create single-ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)
try:
    while True:
        print("{:>5.3f}".format(chan0.voltage))
        sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

# Notes:
# Air => ca 2.3 - 2.4 V
# Water => 0.9 - 0.95
# Complete dry soil => 2.1 - 2.2
# Complete wet soil => 0.93 - 0.96
# Min moisture: 1.0 => 1.2
# Max moisture: 2.0 => 1.5.

