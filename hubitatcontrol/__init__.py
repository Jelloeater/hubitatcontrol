"""Hubitat Maker API"""
__version__ = "0.1.1"

from hubitatcontrol.lights import *


# TODO Add hub get function

def lookup_device(hub, device_lookup):
    d = hub.get_device(device_lookup)
    if d['type'] == 'Advanced Zigbee RGBW Bulb':
        return Advanced_Zigbee_RGBW_Bulb(device_from_hub=d, hub=hub)
