import logging
import os
from importlib import metadata
from importlib.metadata import PackageNotFoundError

import keyring
import typer
from dotenv import load_dotenv

from hubitatcontrol import get_hub

app_name = "hubitatcontrol"

try:
    version = metadata.version(app_name)
except PackageNotFoundError:
    logging.warning('Package not installed')
    version = '0'

app = typer.Typer(
    no_args_is_help=True,
    help='Hubitat Control CLI Interface',
    epilog=f'Version: {version} \n Project: https://github.com/Jelloeater/hubitatcontrol',
)


def check_keyring():
    for i in ['HUBITAT_HOST', 'HUBITAT_API_TOKEN', 'HUBITAT_API_APP_ID']:
        if keyring.get_password(app_name, i) is None:
            raise Exception('Empty Keyring')


def hub_from_keyring():
    check_keyring()
    host_env = keyring.get_password("hubitatcontrol", "HUBITAT_HOST")
    token_env = keyring.get_password("hubitatcontrol", "HUBITAT_API_TOKEN")
    app_id_env = keyring.get_password("hubitatcontrol", "HUBITAT_API_APP_ID")
    cloud_token_env = keyring.get_password("hubitatcontrol", "HUBITAT_CLOUD_TOKEN")
    if cloud_token_env is None:
        cloud_token_env = None
    return get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token_env)


@app.command()
def ls():
    """
    Prints current devices from system keyring
    """

    print_device_list_types(hub_from_keyring())


@app.command()
def on(device_id: int):
    """
    Turn on a device via it's Device ID
    """

    hub_in = hub_from_keyring()
    device = hub_in.get_device_id(device_id)
    import hubitatcontrol.hub

    dev = hubitatcontrol.lookup_device(hub_in, device['name'])

    dev.turn_on()


@app.command()
def off(device_id: int):
    """
    Turn on a device via it's Device ID
    """

    hub_in = hub_from_keyring()
    device = hub_in.get_device_id(device_id)
    import hubitatcontrol.hub

    dev = hubitatcontrol.lookup_device(hub_in, device['name'])

    dev.turn_off()


@app.command()
def level(device_id: int, level: int):
    """Turn on a device via it's Device ID"""

    hub_in = hub_from_keyring()
    device = hub_in.get_device_id(device_id)
    import hubitatcontrol.hub

    dev = hubitatcontrol.lookup_device(hub_in, device['name'])

    dev.set_level(level)


@app.command()
def load_env_to_keyring():
    """
    Load .env file at exec location to keyring
    """

    if not os.path.exists('.env'):
        raise FileNotFoundError('.env file missing')

    load_dotenv('.env')
    # Check for empty keys
    for i in ['HUBITAT_HOST', 'HUBITAT_API_TOKEN', 'HUBITAT_API_APP_ID']:
        if os.getenv(i) is None:
            raise Exception('Please fill in .env file')

    # Set keys
    for i in ['HUBITAT_HOST', 'HUBITAT_API_TOKEN', 'HUBITAT_API_APP_ID', 'HUBITAT_CLOUD_TOKEN']:
        keyring.set_password(app_name, i, str(os.getenv(i)))


@app.command()
def clear_keyring():
    """
    Clear Keyring passwords
    """

    app_name = "hubitatcontrol"
    key_list = ['HUBITAT_HOST', 'HUBITAT_API_TOKEN', 'HUBITAT_API_APP_ID', 'HUBITAT_CLOUD_TOKEN']
    for i in key_list:
        keyring.delete_password(app_name, i)


def print_device_list_types(hub_in):
    """Converts hub object input to pretty table console output"""
    import json

    import prettytable

    obj_to_table = hub_in.devices
    for i in obj_to_table:
        # Clear out extra info
        del i['capabilities']
        del i['attributes']
        del i['commands']
        del i['model']
        del i['manufacturer']
        del i['date']

    print(prettytable.from_json(json.dumps(obj_to_table)))


def hub_creds(host_env, token_env, app_id_env):
    return get_hub(host=host_env, token=token_env, app_id=app_id_env)


if __name__ == "__main__":
    app()
