# Actual control
import time

from device.sensor.dht import dht as dht_sensor
from device.sensor.moisture import moisture as moisture_sensor
from device.switch.light import light
from device.switch.heater import heater
from device.motor.window_servo import window_servo
from logger import logger

def run():
    # get sensor values
    humidity, temperature = dht_sensor.get_values()
    moisture = moisture_sensor.get_moisture()
    light_status = light.get_state()
    heater_status = heater.get_state()

    # log sensor values


    # control devices.
    pass
