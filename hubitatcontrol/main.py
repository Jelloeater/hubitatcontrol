from hubitatcontrol.lights import *


def lookup_device(hub, device_lookup):
    d = hub.get_device(device_lookup)
    if d['type'] == 'Advanced Zigbee RGBW Bulb':
        return Advanced_Zigbee_RGBW_Bulb(device_from_hub=d, hub=hub)
