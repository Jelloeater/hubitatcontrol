"""Hubitat Maker API"""
__version__ = "0.1.0"

import time
from typing import Callable

import requests


class Hub:
    def __init__(self, host, token, app_id, cloud_id=None):
        self.host = host
        self.cloud_id = cloud_id
        self.token = token
        self.app_id = app_id
        if cloud_id:
            self.base_url_prefix = self.host + "/api/" + self.cloud_id + "/apps/" + self.app_id + "/devices"
        else:
            self.base_url_prefix = self.host + "/apps/api/" + self.app_id + "/devices"

    @property
    def devices(self) -> list:
        r = requests.get(
            url=self.base_url_prefix, params={"access_token": self.token}
        )
        return r.json()

    def get_device(self, name: str) -> object:
        for i in self.devices:
            if i['label'] == name:
                return i

    # TODO Work on returning class obj from Hub call
    # def return_dev_class(self, i) -> object:
    #     d = Device(self, i)
    #     if d.type == 'Advanced Zigbee RGBW Bulb':
    #         x = Advanced_Zigbee_RGBW_Bulb(self, d)
    #         return Advanced_Zigbee_RGBW_Bulb(self, device_from_hub=d)


class Device:
    def __init__(self, hub: Hub, device_from_hub: dict):
        self.token = hub.token
        self.base_url_prefix = hub.base_url_prefix
        self.name = device_from_hub['name']
        self.label = device_from_hub['label']
        self.type = device_from_hub['type']
        self.id = device_from_hub['id']

    @property
    def commands(self):
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/commands", params={"access_token": self.token}
        )
        return r.json()

    @property
    def capabilities(self):
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/capabilities", params={"access_token": self.token}
        )
        return r.json()[0]

    @property
    def history(self) -> requests.Response:
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/events", params={"access_token": self.token}
        )
        return r.json()

    @property
    def attributes(self) -> requests.Response:
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id), params={"access_token": self.token}
        )
        return r.json()['attributes']

    def send_device_command(self, command: str, secondary_command: str = None) -> requests.Response:
        if secondary_command is None:
            r = requests.get(
                url=self.base_url_prefix + "/" + str(self.id) + "/" + command, params={"access_token": self.token}
            )
        else:
            r = requests.get(
                url=self.base_url_prefix + "/" + str(self.id) + "/" + command + '/' + secondary_command,
                params={"access_token": self.token}
            )
        time.sleep(.5)
        return r.json()
