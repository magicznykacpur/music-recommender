import os


def setup_env_vars():
    env_file = open(".env").read()
    env_vars = env_file.split("\n")

    for var in env_vars:
        parts = var.split("=")
        os.environ[parts[0]] = parts[1]
