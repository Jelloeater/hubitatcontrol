from importlib import metadata

import typer

from hubitatcontrol import get_hub

version = metadata.version("hubitatcontrol")

app = typer.Typer(
    no_args_is_help=True,
    help='Hubitat Control CLI Interface',
    epilog=f'Version: {version} \n Project: https://github.com/Jelloeater/hubitatcontrol',
)


@app.command()
def print_devices_env():
    """
    Loads .env file at current location and prints current devices
    """
    import os

    from dotenv import load_dotenv

    load_dotenv()

    host_env = os.getenv("HUBITAT_HOST")
    token_env = os.getenv("HUBITAT_API_TOKEN")
    app_id_env = os.getenv("HUBITAT_API_APP_ID")
    cloud_token_env = os.getenv("HUBITAT_CLOUD_TOKEN")
    h = get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token_env)
    print_device_list_types(h)


@app.command()
def print_devices_cli(host_env, token_env, app_id_env: int, cloud_token_env=typer.Argument(None)):
    """
    Prints current devices from CLI input
    """
    h = get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token_env)
    print_device_list_types(h)


@app.command()
def ls():
    """
    Prints current devices from system keyring
    """
    import keyring

    host_env = keyring.get_password("hubitatcontrol", "HUBITAT_HOST")
    token_env = keyring.get_password("hubitatcontrol", "HUBITAT_API_TOKEN")
    app_id_env = keyring.get_password("hubitatcontrol", "HUBITAT_API_APP_ID")
    cloud_token_env = keyring.get_password("hubitatcontrol", "HUBITAT_CLOUD_TOKEN")
    if cloud_token_env == 'None':
        cloud_token_env = None
    h = get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token_env)
    print_device_list_types(h)


@app.command()
def load_env_to_keyring():
    """
    Load .env to keyring
    """

    import os
    from dotenv import load_dotenv

    # load_dotenv()
    load_dotenv()

    import keyring

    app_name = "hubitatcontrol"
    key_list = ['HUBITAT_HOST', 'HUBITAT_API_TOKEN', 'HUBITAT_API_APP_ID', 'HUBITAT_CLOUD_TOKEN']
    for i in key_list:
        if i is not None:
            keyring.set_password(app_name, i, str(os.getenv(i)))


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
