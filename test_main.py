
import pytest
from dotenv import load_dotenv
import Hubitat as Hubitat

load_dotenv()


def test_creds():
    import os
    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


def test_hub_get():
    h = Hubitat.Hub()
    if h.devices is not None:
        pytest.hub = h
        assert True
    else:
        pytest.hub = None
        assert False


def test_lookup_device():
    h = Hubitat.Hub()
    p = h.get_device('Porch')
    assert p is not None


def test_init_device():
    h = Hubitat.Hub()
    d = h.get_device('Porch')
    device = Hubitat.Device(d)
    assert device is not None


def test_send_device_command():
    h = Hubitat.Hub()
    d = h.get_device('Porch')
    test_bulb = Hubitat.Bulb(d)

    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
