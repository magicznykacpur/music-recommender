import spotipy
from spotipy.oauth2 import SpotifyOAuth
from env.setup_env import setup_env_vars
from user.user import User


username = "magicznykacpur"

def main():
    setup_env_vars()
    scope = "playlist-modify-public user-library-read"

    client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username))

    user = User(username, client)


if __name__ == "__main__":
    main()
