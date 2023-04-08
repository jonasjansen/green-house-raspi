# Entrypoint for greenhouse control
import yaml

from api import zigbee

CONFIG_FILE_PATH = "config.yaml"


def load_configuration():
    with open(CONFIG_FILE_PATH, "r") as f:
        return yaml.safe_load(f)


configuration = load_configuration()
print(configuration)
zigbee.test()
