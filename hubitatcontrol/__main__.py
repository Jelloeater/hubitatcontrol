import typer
from hubitatcontrol import get_hub

app = typer.Typer(no_args_is_help=True)


@app.command()
def print_devices_env():
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
    h = get_hub(host=host_env, token=token_env, app_id=app_id_env, cloud_token=cloud_token_env)
    print_device_list_types(h)


def print_device_list_types(hub_in):
    """Converts hub object input to pretty table console output"""
    import prettytable
    import json

    obj_to_table = hub_in.devices
    for i in obj_to_table:
        # Clear out extra info
        del i['capabilities']
        del i['attributes']
        del i['commands']

    print(prettytable.from_json(json.dumps(obj_to_table)))


def hub_creds(host_env, token_env, app_id_env):
    return get_hub(host=host_env, token=token_env, app_id=app_id_env)


if __name__ == "__main__":
    app()
