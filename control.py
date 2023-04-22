# Actual control
from time import sleep

from device.sensor.dht import dht as dht_sensor
from device.sensor.moisture import moisture as moisture_sensor
from device.switch.light import light
from device.switch.heater import heater
from device.motor.window_servo import window_servo
from device.motor.humidity_pump import humidity_pump
from device.motor.watering_pump import watering_pump
from device.camera.picture import picture

from config_provider import config
from logger import logger
import datetime


def run():
    # take picture
    picture.take()

    # get sensor values
    humidity, temperature = dht_sensor.get_values()
    moisture = moisture_sensor.get_moisture()
    light_status = light.get_state()
    heater_status = heater.get_state()

    # current hour
    now = datetime.datetime.now()
    current_hour = now.hour

    # log sensor values
    logger.info("humidity: " + str(humidity))
    logger.info("temperature: " + str(temperature))
    logger.info("moisture: " + str(moisture))
    logger.info("light_status: " + str(light_status))
    logger.info("heater_status: " + str(heater_status))

    # do not run any pumps during night
    # light
    if config.get_config('CONTROL/LIGHT/START') < current_hour < config.get_config('CONTROL/LIGHT/END'):
        logger.info("Turn On Light")
        light.turn_on()
    else:
        logger.info("Turn Off Light")
        light.turn_off()

    # temperature
    if temperature <= config.get_config('CONTROL/TEMPERATURE/MIN'):
        logger.info("Turn On Heat")
        heater.turn_on()
    elif temperature >= config.get_config('CONTROL/TEMPERATURE/MAX'):
        logger.info("Turn Off Heat")
        heater.turn_off()

    # run pumps only in defined hours for security reasons.
    if config.get_config('CONTROL/PUMP/START') < current_hour < config.get_config('CONTROL/PUMP/END'):

        # humidity
        if humidity <= config.get_config('CONTROL/HUMIDITY/MIN'):
            logger.info("Turn On Humidity")
            humidity_pump.run(15)
            logger.info("Close Window")
            window_servo.close_window()
        elif humidity >= config.get_config('CONTROL/HUMIDITY/MAX'):
            logger.info("Open Window")
            window_servo.open_window()
        else:
            logger.info("Close Window")
            window_servo.close_window()

        # moisture
        if float(moisture) >= float(config.get_config('CONTROL/MOISTURE/THRESHOLD')):
            logger.info("Turn On Moisture")
            humidity_pump.run(10)
            watering_pump.run(10)
