# Entrypoint for greenhouse control
import yaml

from api import zigbee

CONFIG_FILE_PATH = "config.yaml"


zigbee.test2()
