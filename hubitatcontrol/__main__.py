import typer
from hubitatcontrol import get_hub


def print_device_list_types():
    import os

    from dotenv import load_dotenv

    envs = load_dotenv()
    if envs:
        host_env = os.getenv("HUBITAT_HOST")
        token_env = os.getenv("HUBITAT_API_TOKEN")
        app_id_env = os.getenv("HUBITAT_API_APP_ID")
        h = get_hub(host=host_env, token=token_env, app_id=app_id_env)
    else:
        h = hub_creds()
    for i in h.devices:
        d = h.get_device(i)
        # TODO Need to finish device type output


def hub_creds(host_env, token_env, app_id_env):
    return get_hub(host=host_env, token=token_env, app_id=app_id_env)


if __name__ == "__main__":
    typer.run(print_device_list_types)
