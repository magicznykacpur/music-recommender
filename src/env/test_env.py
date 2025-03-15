import os

from setup_env import setup_env_vars


class TestEnv:
    def test_setup_env_vars(self):
        setup_env_vars()

        assert os.environ["SPOTIPY_CLIENT_ID"] != ""
        assert os.environ["SPOTIPY_CLIENT_SECRET"] != ""
