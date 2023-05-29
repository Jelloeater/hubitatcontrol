import os
import random
import time

from dotenv import load_dotenv

import hubitatcontrol
from hubitatcontrol import *


def get_hub():
    load_dotenv()
    host_env = os.getenv("HUBITAT_HOST")
    token_env = os.getenv("HUBITAT_API_TOKEN")
    app_id_env = os.getenv("HUBITAT_API_APP_ID")
    cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")
    return Hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token)


def get_device_of_type(device_type: str):
    h = get_hub()
    for i in h.devices:
        if i["type"] == device_type:
            return i


def test_creds():
    load_dotenv()
    import os

    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


class TestDeviceType:
    def test_get_all_temperature_sensors(self):
        h = get_hub()
        x = hubitatcontrol.GetDevices(h).TemperatureSensor()
        # TODO -> Fix temp data get from EcoBee <-
        assert x is not None


class TestDevices:
    def test_device_bulb(self):
        t = get_device_of_type("Virtual RGBW Light")
        t = hubitatcontrol.GetDevice(get_hub(), t).cast_device()
        state = t.switch
        temp = t.color_temp
        hue = t.hue
        sat = t.saturation

        t.turn_on()
        assert t.switch == "on"
        t.turn_off()
        assert t.switch == "off"
        t.turn_on()
        assert t.switch == "on"

        t.set_color_temp(3205)
        assert t.color_temp == 3205
        t.set_color_temp(temp)

        t.set_hue(100)
        assert t.hue == 100
        t.set_hue(hue)

        t.set_saturation(10)
        time.sleep(1)
        assert t.saturation == 10
        t.set_saturation(80)
        time.sleep(1)
        assert t.saturation == 80
        t.set_hue(sat)

        if state == "on":
            t.turn_on()
        else:
            t.turn_off()

    def test_device_outlet(self):
        t = get_device_of_type("Virtual Switch")
        t = hubitatcontrol.GetDevice(get_hub(), t).cast_device()
        state = t.switch
        t.turn_off()
        assert t.switch == "off"
        t.turn_on()
        assert t.switch == "on"
        if state == "on":
            t.turn_on()
        else:
            t.turn_off()

    def test_device_dimmer(self):
        d = get_device_of_type("Virtual Dimmer")
        d = hubitatcontrol.GetDevice(get_hub(), d).cast_device()

        assert d
        state_l = d.switch  # To set light back where they were
        state = d.level
        d.set_level(25)
        assert d.level == 25
        d.set_level(50)
        assert d.level == 50
        d.set_level(state)
        if state_l == "on":
            d.turn_on()
        else:
            d.turn_off()

    def test_temp_sensor(self):
        d = get_device_of_type("Virtual Temperature Sensor")
        d = hubitatcontrol.GetDevice(get_hub(), d).cast_device()

        assert d.temperature == 72

    def test_set_color_map(self):
        d = get_device_of_type("Virtual RGBW Light")
        d = hubitatcontrol.GetDevice(get_hub(), d).cast_device()

        hue = random.randint(0, 100)
        saturation = random.randint(0, 100)
        level = random.randint(0, 100)

        d.set_color(hue=hue, saturation=saturation, level=level)
        assert d.level == level
        assert d.hue == hue
        assert d.saturation == saturation
