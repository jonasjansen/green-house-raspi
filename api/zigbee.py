import requests

from config_provider import config


def test():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    print(response.json())


def test2():
    print(config.get_config('ZIGBEE/API_IP'))
    print(config.get_config('ZIGBEE/ID/LIGHT'))
