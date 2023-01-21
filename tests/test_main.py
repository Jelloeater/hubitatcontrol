import logging
import os
from time import sleep

from dotenv import load_dotenv

import hubitatcontrol
from hubitatcontrol import *
from hubitatcontrol import Device

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")


def test_creds():
    import os
    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


def test_hub_get():
    h = Hub(host=host_env, token=token_env, app_id=app_id_env)
    if h.devices is not None:
        assert True
    else:
        assert False


def test_device_bulb():
    test_dev = None
    h = Hub(host=host_env, token=token_env, app_id=app_id_env)
    for i in h.devices:
        if i['type'] == 'Advanced Zigbee RGBW Bulb':
            test_dev: Device = Device(h, i)
            assert test_dev
            break

    test_bulb = lookup_device(h, test_dev.label)
    state = test_bulb.switch
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    if state == 'on':
        test_bulb.turn_on()
    else:
        test_bulb.turn_off()


def test_device_outlet():
    test_dev = None
    h = Hub(host=host_env, token=token_env, app_id=app_id_env)
    for i in h.devices:
        if i['type'] == 'Generic Zigbee Outlet':
            test_dev: Device = Device(h, i)
            assert test_dev
            break

    t = lookup_device(h, test_dev.label)

    state = t.switch
    t.turn_off()
    assert t.switch == 'off'
    t.turn_on()
    assert t.switch == 'on'
    if state == 'on':
        t.turn_on()
    else:
        t.turn_off()


def test_device_dimmer():
    test_dev = None
    h = Hub(host=host_env, token=token_env, app_id=app_id_env)

    for i in h.devices:
        if i['type'] == 'Leviton DZ6HD Z-Wave Dimmer':
            test_dev: Device = Device(h, i)
            assert test_dev
            break

    d = lookup_device(h, test_dev.label)
    assert d
    state = d.level
    d.set_level(25)
    assert d.level == 25
    d.set_level(50)
    assert d.level ==50
    d.set_level(state)

