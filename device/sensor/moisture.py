from config_provider import config


# install via 'sudo pip install Adafruit-DHT'
# NOTE: Is deprecated. Might want to replace it with https://pypi.org/project/adafruit-circuitpython-dht/

class Moisture:

    def __init__(self):
        self.gpio = config.get_config('GPIO/MOISTURE/DATA_PIN')
        self.moisture = 0

    def get_moisture(self):
        # TODO
        pass


moisture = Moisture()
