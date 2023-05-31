"""Hubitat Maker API"""
import os

from dotenv import load_dotenv

import hubitatcontrol.generic as generic
import hubitatcontrol.lights as lights
import hubitatcontrol.sensors as sensors
from hubitatcontrol.hub import Hub


class GetSingleDevice:
    def __init__(self, hub_in: Hub):
        self.hub = hub_in

    def name(self, device_name: str):
        for i in self.hub.devices:
            if i["name"] == device_name:
                return DeviceInit(device_in=i, hub_in=self.hub).cast_device()

    def id(self, device_id: int):
        for i in self.hub.devices:
            if i["id"] == str(device_id):
                return DeviceInit(device_in=i, hub_in=self.hub).cast_device()


class GetDevices:
    def __init__(self, hub_in: Hub):
        self.hub = hub_in

    def __get_devices_from_capabilities__(self, capabilities_list: [str]):
        device_list = []
        for i in self.hub.devices:
            if all([x in i["capabilities"] for x in capabilities_list]):
                d = DeviceInit(self.hub, i).cast_device()
                device_list.append(d)
        return device_list

    def TemperatureSensor(self) -> list[sensors.TemperatureSensor]:
        return self.__get_devices_from_capabilities__(sensors.TemperatureSensor.spec)

    def EnvironmentalSensor(self) -> list[sensors.EnvironmentalSensor]:
        return self.__get_devices_from_capabilities__(sensors.EnvironmentalSensor.spec)

    def Switch(self) -> list[generic.Switch]:
        return self.__get_devices_from_capabilities__(generic.Switch.spec)

    def Outlet(self) -> list[generic.ZigbeeOutlet]:
        return self.__get_devices_from_capabilities__(generic.ZigbeeOutlet.spec)

    def Dimmer(self) -> list[lights.Dimmer]:
        return self.__get_devices_from_capabilities__(lights.Dimmer.spec)

    def Bulb(self) -> list[lights.Bulb]:
        return self.__get_devices_from_capabilities__(lights.Bulb.spec)

    def ColorTempBulb(self) -> list[lights.ColorTempBulb]:
        return self.__get_devices_from_capabilities__(lights.ColorTempBulb.spec)

    def RGBWBulb(self) -> list[lights.RGBWBulb]:
        return self.__get_devices_from_capabilities__(lights.RGBWBulb.spec)


class DeviceInit:
    def __init__(self, hub_in: Hub, device_in: generic.Device):
        self.hub = hub_in
        self.device = device_in

    def cast_device(self):
        """The order here is very important that we cast the device properly based on increasing complexity /
        functionality"""
        c = self.device["capabilities"]

        if all([x in c for x in sensors.TemperatureSensor.spec]):
            return sensors.TemperatureSensor(self.hub, self.device)

        if all([x in c for x in sensors.EnvironmentalSensor.spec]):
            return sensors.EnvironmentalSensor(self.hub, self.device)

        if all([x in c for x in generic.ZigbeeOutlet.spec]):
            return generic.ZigbeeOutlet(self.hub, self.device)

        if all([x in c for x in lights.RGBWBulb.spec]):
            return lights.RGBWBulb(self.hub, self.device)

        if all([x in c for x in lights.ColorTempBulb.spec]):
            return lights.ColorTempBulb(self.hub, self.device)

        if all([x in c for x in lights.Dimmer.spec]):
            return lights.Dimmer(self.hub, self.device)

        if all([x in c for x in lights.Bulb.spec]):
            return lights.Bulb(self.hub, self.device)

        if all([x in c for x in lights.Switch.spec]):
            return lights.Switch(self.hub, self.device)


def get_hub_envs() -> Hub:
    """
    Generates a Hub object from local environmental variables
    """
    load_dotenv()
    host_env = os.getenv("HUBITAT_HOST")
    token_env = os.getenv("HUBITAT_API_TOKEN")
    app_id_env = os.getenv("HUBITAT_API_APP_ID")
    cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")
    return Hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token)
