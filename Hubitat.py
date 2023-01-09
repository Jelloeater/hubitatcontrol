import os
import time

import requests

class Hubitat:
    def __init__(self, cloud: bool = False):
        self.host = os.getenv("HUBITAT_HOST")
        self.cloud_id = os.getenv("HUBITAT_CLOUD_ID")
        self.token = os.getenv("HUBITAT_API_TOKEN")
        self.app_id = os.getenv("HUBITAT_API_APP_ID")
        if cloud:
            self.base_url_prefix = self.host + "/api/" + self.cloud_id + "/apps/" + self.app_id + "/devices"
        else:
            self.base_url_prefix = self.host + "/apps/api/" + self.app_id + "/devices"


class Hub(Hubitat):
    def __init__(self):
        super().__init__()

    @property
    def devices(self) -> list:
        r = requests.get(
            url=self.base_url_prefix, params={"access_token": self.token}
        )
        return r.json()

    def get_device(self, name: str) -> int:
        for i in self.devices:
            if i['label'] == name:
                return i


class Device(Hubitat):
    def __init__(self, device_from_hub):
        super().__init__()
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


class Bulb(Device):
    def __init__(self, device_from_hub):
        super().__init__(device_from_hub)

    @property
    def switch(self):
        return [x for x in self.attributes if "switch" in x["name"]][0]['currentValue']

    def turn_on(self):
        self.send_device_command(command='on')

    def turn_off(self):
        self.send_device_command(command='off')
