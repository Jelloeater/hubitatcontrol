"""Hubitat Maker API"""
import hubitatcontrol.generic
import hubitatcontrol.lights
import hubitatcontrol.sensors
from hubitatcontrol.hub import Hub


class GetDevices:
    def __init__(self, hub_in: Hub):
        self.hub = hub_in

    def __get_devices_from_capabilities__(self, capabilities_list: [str]):
        device_list = []
        for i in self.hub.devices:
            if all([x in i["capabilities"] for x in capabilities_list]):
                d = GetDevice(self.hub, i).cast_device()
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


class GetDevice:
    def __init__(self, hub_in: Hub, device_in: hubitatcontrol.generic.Device):
        self.hub = hub_in
        self.device = device_in

    def cast_device(self):
        """The order here is very important that we cast the device properly based on increasing complexity /
        functionality"""
        c = self.device["capabilities"]

        if all([x in c for x in sensors.TemperatureSensor.spec]):
            return hubitatcontrol.sensors.TemperatureSensor(self.hub, self.device)

        if all([x in c for x in sensors.EnvironmentalSensor.spec]):
            return hubitatcontrol.sensors.EnvironmentalSensor(self.hub, self.device)

        if all([x in c for x in generic.ZigbeeOutlet.spec]):
            return hubitatcontrol.generic.ZigbeeOutlet(self.hub, self.device)

        if all([x in c for x in lights.RGBWBulb.spec]):
            return hubitatcontrol.lights.RGBWBulb(self.hub, self.device)

        if all([x in c for x in lights.ColorTempBulb.spec]):
            return hubitatcontrol.lights.ColorTempBulb(self.hub, self.device)

        if all([x in c for x in lights.Dimmer.spec]):
            return hubitatcontrol.lights.Dimmer(self.hub, self.device)

        if all([x in c for x in lights.Bulb.spec]):
            return hubitatcontrol.lights.Bulb(self.hub, self.device)

        if all([x in c for x in ["Switch"]]):
            return hubitatcontrol.lights.Switch(self.hub, self.device)
