"""Hubitat Maker API"""

import hubitatcontrol.generic
import hubitatcontrol.lights
import hubitatcontrol.sensors
from hubitatcontrol.hub import Hub


def get_device_type(device_in: hubitatcontrol.hub.Device, hub_in: hubitatcontrol.hub):
    if device_in is None:
        raise Exception("Device Not Found")
    if "ColorControl" in device_in["capabilities"] and "ColorMode" in device_in["capabilities"]:
        return hubitatcontrol.lights.RGBWBulb(device_from_hub=device_in, hub=hub_in)
    if "ColorTemperature" in device_in["capabilities"]:
        return hubitatcontrol.lights.ColorTempBulb(device_from_hub=device_in, hub=hub_in)
    if "ChangeLevel" in device_in["capabilities"]:
        return hubitatcontrol.lights.Bulb(device_from_hub=device_in, hub=hub_in)
    if "SwitchLevel" in device_in["capabilities"]:
        return hubitatcontrol.lights.Dimmer(device_from_hub=device_in, hub=hub_in)
    if "PowerMeter" in device_in["capabilities"] and "Outlet" in device_in["capabilities"]:
        return hubitatcontrol.generic.ZigbeeOutlet(device_from_hub=device_in, hub=hub_in)
    if "Switch" in device_in["capabilities"]:
        return hubitatcontrol.generic.Switch(device_from_hub=device_in, hub=hub_in)
    if (
        "TemperatureMeasurement" in device_in["capabilities"]
        and "RelativeHumidityMeasurement" in device_in["capabilities"]
    ):
        return hubitatcontrol.sensors.EnvironmentalSensor(device_from_hub=device_in, hub=hub_in)
    if "TemperatureMeasurement" in device_in["capabilities"]:
        return hubitatcontrol.sensors.TemperatureSensor(device_from_hub=device_in, hub=hub_in)


def get_hub(host, token, app_id, cloud_token=None) -> Hub:
    return Hub(host=host, token=token, app_id=app_id, cloud_token=cloud_token)


def lookup_device(hub_in, device_lookup):
    """
    Takes device NAME, not ID for lookup
    """

    return get_device_type(
        device_in=hub_in.get_device(device_lookup), hub_in=hub_in
    )  # Fall through return # pragma: no cover


def lookup_device_id(hub_in, device_id):
    """
    Takes device ID for lookup
    """
    return get_device_type(
        device_in=hub_in.get_device_id(device_id), hub_in=hub_in
    )  # Fall through return # pragma: no cover


# TODO Refactor this to be dry
def get_all_temperature_sensors(hub_in: hubitatcontrol.hub) -> list[hubitatcontrol.sensors.TemperatureSensor]:
    """Returns list of all hub devices with associated helper functions"""
    device_list = []
    for i in hub_in.devices:
        if "TemperatureMeasurement" in i["capabilities"]:
            device_list.append(get_device_type(i, hub_in))
    return device_list


def get_all_environmental_sensors(hub_in: hubitatcontrol.hub) -> list[hubitatcontrol.sensors.EnvironmentalSensor]:
    """Returns list of all hub devices with associated helper functions"""
    device_list = []
    for i in hub_in.devices:
        if ("RelativeHumidityMeasurement" in i["capabilities"]) and ("TemperatureMeasurement" in i["capabilities"]):
            device_list.append(get_device_type(i, hub_in))
    return device_list
