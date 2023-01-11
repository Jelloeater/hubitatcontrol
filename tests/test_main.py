import os
from dotenv import load_dotenv
import src.hubitatcontrol as Hubitat
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


def test_lookup_device():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    p = h.get_device('Porch')
    assert p is not None


def test_init_device():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    d = h.get_device('Porch')
    device = Hubitat.Device(hub=h, device_from_hub=d)
    assert device is not None


def test_send_device_command():
    h = Hubitat.Hub(host=host_env, token=token_env, app_id=app_id_env)
    d = h.get_device('Porch')
    test_bulb = Hubitat.Bulb(h, d)

    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
