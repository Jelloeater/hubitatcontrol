import os
import pytest
from dotenv import load_dotenv

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")
cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")


# CLI Tests
@pytest.mark.skipif(load_dotenv() is False, reason='No env file found')
def test_cli_keyring():
    import hubitatcontrol.__main__ as cli

    cli.load_env_to_keyring()
    cli.ls()


@pytest.mark.skipif(load_dotenv() is False, reason='No env file found')
def test_cli_on():
    import hubitatcontrol.__main__ as cli

    cli.load_env_to_keyring()
    cli.on(257)
