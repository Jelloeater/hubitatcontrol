"""Hubitat Maker API"""

import hubitatcontrol.generic
import hubitatcontrol.lights
import hubitatcontrol.sensors
from hubitatcontrol.hub import Hub


def get_hub(host, token, app_id, cloud_token=None) -> Hub:
    return Hub(host=host, token=token, app_id=app_id, cloud_token=cloud_token)


def lookup_device(hub_in, device_lookup):
    # TODO Refactor to use ID, and and add interface for name search
    """
    Takes device NAME, not ID for lookup
    """
    d = hub_in.get_device(device_lookup)
    if d is None:
        raise Exception("Device Not Found")
    if "ColorControl" in d["capabilities"] and "ColorMode" in d["capabilities"]:
        return hubitatcontrol.lights.RGBWBulb(device_from_hub=d, hub=hub_in)
    if "ColorTemperature" in d["capabilities"]:
        return hubitatcontrol.lights.ColorTempBulb(device_from_hub=d, hub=hub_in)
    if "ChangeLevel" in d["capabilities"]:
        return hubitatcontrol.lights.Bulb(device_from_hub=d, hub=hub_in)
    if "SwitchLevel" in d["capabilities"]:
        return hubitatcontrol.lights.Dimmer(device_from_hub=d, hub=hub_in)
    if "PowerMeter" in d["capabilities"] and "Outlet" in d["capabilities"]:
        return hubitatcontrol.generic.ZigbeeOutlet(device_from_hub=d, hub=hub_in)
    if "Switch" in d["capabilities"]:
        return hubitatcontrol.generic.Switch(device_from_hub=d, hub=hub_in)
    if "TemperatureMeasurement" in d["capabilities"]:
        return hubitatcontrol.sensors.TemperatureSensor(device_from_hub=d, hub=hub_in)
    return d  # Fall through return # pragma: no cover


def get_all_devices(hub_in: hub) -> list[hubitatcontrol.hub.Device]:
    """Returns list of all hub devices with associated helper functions"""
    device_list = []
    for i in hub_in.devices:
        device_list.append(lookup_device(hub_in, i['name']))
    return device_list
