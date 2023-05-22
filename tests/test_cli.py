import os

import pytest
from dotenv import load_dotenv

from hubitatcontrol import __main__ as cli
from tests.test_main import get_device_of_type

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")
cloud_token = os.getenv("HUBITAT_CLOUD_TOKEN")


class TestCLI:
    @classmethod
    def setup_class(cls):
        try:
            cli.clear_keyring()
        except:
            pass
        cli.load_env_to_keyring()

    @classmethod
    def teardown_class(cls):
        cli.clear_keyring()

    # CLI Tests
    # TODO Add .env file generator for GH Actions test coverage
    @pytest.mark.skipif(load_dotenv('.env') is False, reason='No env file found')
    def test_cli_keyring(self):
        cli.ls()

    @pytest.mark.skipif(load_dotenv('.env') is False, reason='No env file found')
    def test_cli_on(self):
        test_bulb = get_device_of_type("Virtual RGBW Light")
        cli.on(test_bulb['id'])
