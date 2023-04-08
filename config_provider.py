# Entrypoint for greenhouse control
import yaml

CONFIG_FILE_PATH = "config.yaml"


class ConfigProvider:
    def __init__(self):
        self.config = dict()

    def get_config(self, path=None):
        if not self.config:
            self.load_config()
        # Get config from path. Example path 'ZIGBEE/ID/LIGHT' for dict {'ZIGBEE': {'ID': {'LIGHT':0}}} returns 0
        if path:
            sub_config = self.config
            for part in path.split('/'):
                if part in sub_config:
                    sub_config = sub_config[part]
                else:
                    print("ERROR: could not find", part, "in", sub_config, "which is in", self.config)
                    return ''
            return sub_config
        else:
            return self.config

    def load_config(self):
        with open(CONFIG_FILE_PATH, "r") as f:
            self.config = yaml.safe_load(f)


config = ConfigProvider()
