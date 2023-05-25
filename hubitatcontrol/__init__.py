"""Hubitat Maker API"""

import hubitatcontrol.generic
import hubitatcontrol.lights
import hubitatcontrol.sensors
from hubitatcontrol.hub import Hub


class GetDevices:
    def __init__(self, hub_in: hubitatcontrol.Hub):
        self.hub = hub_in

    def __get_devices_from_capabilities__(self, capabilities_list: [str]):
        device_list = []
        for i in self.hub.devices:
            if all([x in i["capabilities"] for x in capabilities_list]):
                device_list.append(i)
        return device_list

    def TemperatureSensor(self) -> list[hubitatcontrol.sensors.TemperatureSensor]:
        return self.__get_devices_from_capabilities__(["TemperatureMeasurement"])

    def EnvironmentalSensor(self) -> list[hubitatcontrol.sensors.EnvironmentalSensor]:
        return self.__get_devices_from_capabilities__(["RelativeHumidityMeasurement", "TemperatureMeasurement"])

    def Switch(self) -> list[hubitatcontrol.generic.Switch]:
        return self.__get_devices_from_capabilities__(["Switch"])

    def Outlet(self) -> list[hubitatcontrol.generic.ZigbeeOutlet]:
        return self.__get_devices_from_capabilities__(["PowerMeter", "Outlet"])

    def Dimmer(self) -> list[hubitatcontrol.lights.Dimmer]:
        return self.__get_devices_from_capabilities__(["SwitchLevel"])

    def Bulb(self) -> list[hubitatcontrol.lights.Bulb]:
        return self.__get_devices_from_capabilities__(["ChangeLevel"])

    def ColorTempBulb(self) -> list[hubitatcontrol.lights.ColorTempBulb]:
        return self.__get_devices_from_capabilities__(["ColorTemperature"])

    def RGBWBulb(self) -> list[hubitatcontrol.lights.RGBWBulb]:
        return self.__get_devices_from_capabilities__(["ColorControl", "ColorMode"])
