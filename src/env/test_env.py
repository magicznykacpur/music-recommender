import os

from setup_env import setup_env_vars


def test_setup_env_vars():
    setup_env_vars()

    assert os.environ["SPOTIPY_CLIENT_ID"] != ""
    assert os.environ["SPOTIPY_CLIENT_SECRET"] != ""


def test_does_not_setup_env_vars():
    assert os.environ["SPOTIPY_CLIENT_ID"] != ""
    assert os.environ["SPOTIPY_CLIENT_SECRET"] != ""
