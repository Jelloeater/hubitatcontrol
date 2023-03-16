import time

import requests

timeout = 10


class Hub:
    def __init__(self, host, token, app_id, cloud_token=None):
        self.host = host
        self.cloud_token = cloud_token
        self.token = token
        self.app_id = app_id
        if cloud_token:
            self.base_url_prefix = self.host + "/api/" + self.cloud_token + "/apps/" + self.app_id + "/devices"
        else:
            self.base_url_prefix = self.host + "/apps/api/" + self.app_id + "/devices"

    @property
    def devices(self) -> list:
        r = requests.get(url=self.base_url_prefix + "/all", params={"access_token": self.token}, timeout=timeout)
        return r.json()

    def get_device(self, name: str):
        for i in self.devices:
            if i["label"] == name:
                return i


class Device:
    def __init__(self, hub: Hub, device_from_hub: dict):
        self.token = hub.token
        self.base_url_prefix = hub.base_url_prefix
        self.name = device_from_hub["name"]
        self.label = device_from_hub["label"]
        self.type = device_from_hub["type"]
        self.id = device_from_hub["id"]

    @property
    def commands(self):
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/commands",
            params={"access_token": self.token},
            timeout=timeout,
        )
        return r.json()

    @property
    def capabilities(self):
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/capabilities",
            params={"access_token": self.token},
            timeout=timeout,
        )
        return r.json()[0]

    @property
    def history(self) -> requests.Response:
        r = requests.get(
            url=self.base_url_prefix + "/" + str(self.id) + "/events",
            params={"access_token": self.token},
            timeout=timeout,
        )
        return r.json()

    @property
    def attributes(self) -> requests.Response:
        r = requests.get(url=self.base_url_prefix + "/" + str(self.id), params={"access_token": self.token}, timeout=10)
        return r.json()["attributes"]

    def send_device_command(self, command: str, secondary_command: str = None) -> requests.Response:
        if secondary_command is None:
            r = requests.get(
                url=self.base_url_prefix + "/" + str(self.id) + "/" + command,
                params={"access_token": self.token},
                timeout=timeout,
            )
        else:
            r = requests.get(
                url=self.base_url_prefix + "/" + str(self.id) + "/" + command + "/" + secondary_command,
                params={"access_token": self.token},
                timeout=timeout,
            )
        time.sleep(0.5)
        return r.json()
