import os
import random

from dotenv import load_dotenv

from hubitatcontrol import *

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")
cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")


def get_device_of_type(device_type: str):
    h = Hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token)
    for i in h.devices:
        if i["type"] == device_type:
            return lookup_device(h, i["label"])


def test_creds():
    import os

    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


def test_device_bulb():
    test_bulb = get_device_of_type("Virtual RGBW Light")
    state = test_bulb.switch
    temp = test_bulb.color_temp
    hue = test_bulb.hue
    sat = test_bulb.saturation

    test_bulb.turn_on()
    assert test_bulb.switch == "on"
    test_bulb.turn_off()
    assert test_bulb.switch == "off"
    test_bulb.turn_on()
    assert test_bulb.switch == "on"

    test_bulb.set_color_temp(3205)
    assert test_bulb.color_temp == 3205
    test_bulb.set_color_temp(temp)

    test_bulb.set_hue(100)
    assert test_bulb.hue == 100
    test_bulb.set_hue(hue)

    test_bulb.set_saturation(10)
    assert test_bulb.saturation == 10
    test_bulb.set_saturation(80)
    assert test_bulb.saturation == 80
    test_bulb.set_hue(sat)

    if state == "on":
        test_bulb.turn_on()
    else:
        test_bulb.turn_off()


def test_device_outlet():
    t = get_device_of_type("Virtual Switch")
    state = t.switch
    t.turn_off()
    assert t.switch == "off"
    t.turn_on()
    assert t.switch == "on"
    if state == "on":
        t.turn_on()
    else:
        t.turn_off()


def test_device_dimmer():
    d = get_device_of_type("Virtual Dimmer")
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


def test_temp_sensor():
    d = get_device_of_type("Virtual Temperature Sensor")
    assert d.temperature == 72


def test_set_color_map():
    test_bulb = get_device_of_type("Virtual RGBW Light")
    hue = random.randint(0, 100)
    saturation = random.randint(0, 100)
    level = random.randint(0, 100)

    test_bulb.set_color(hue=hue, saturation=saturation, level=level)
    assert test_bulb.level == level
    assert test_bulb.hue == hue
    assert test_bulb.saturation == saturation


def test_cli():
    import hubitatcontrol.__main__ as cli

    cli.print_devices_env()


def test_cli_keyring():
    import hubitatcontrol.__main__ as cli

    cli.load_env_to_keyring()
    cli.ls()
    cli.on(1)
