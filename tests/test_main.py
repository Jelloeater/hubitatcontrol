import os
from dotenv import load_dotenv

import hubitatcontrol as Hubitat
import lights

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")


def test_creds():
    import os
    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


def test_hub_get():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    if h.devices is not None:
        assert True
    else:
        assert False


test_device_name = 'Porch'


def test_lookup_device():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    p = h.get_device(test_device_name)
    assert p is not None


def test_init_device():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    d = h.get_device(test_device_name)
    device = Hubitat.Device(hub=h, device_from_hub=d)
    assert device is not None


def test_device_basic():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    d = h.get_device(test_device_name)
    device = Hubitat.Device(hub=h, device_from_hub=d)
    for i in device.commands:
        assert i
    for i in device.capabilities:
        assert i
    for i in device.history:
        assert i
    for i in device.attributes:
        assert i



def test_device_bulb():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    d = h.get_device(test_device_name)
    test_bulb = lights.Advanced_Zigbee_RGBW_Bulb(h, d)

    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
