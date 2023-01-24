"""Hubitat Maker API"""

from hubitatcontrol.generic import *
from hubitatcontrol.hub import Hub
from hubitatcontrol.lights import *


def get_hub(host, token, app_id) -> Hub:
    return Hub(host=host, token=token, app_id=app_id)


def lookup_device(hub_in, device_lookup):
    d = hub_in.get_device(device_lookup)
    if "ColorControl" in d["capabilities"] and "ColorMode" in d["capabilities"]:
        return BulbRGBW(device_from_hub=d, hub=hub_in)
    if "ColorTemperature" in d["capabilities"]:
        return ColorTempBulb(device_from_hub=d, hub=hub_in)
    if "ChangeLevel" in d["capabilities"]:
        return Bulb(device_from_hub=d, hub=hub_in)
    if "PowerMeter" in d["capabilities"] and "Outlet" in d["capabilities"]:
        return ZigbeeOutlet(device_from_hub=d, hub=hub_in)
    if "Switch" in d["capabilities"]:
        return Switch(device_from_hub=d, hub=hub_in)
    return d  # Fall through return


# TODO Add dynamic device return based on capabilities / actions
