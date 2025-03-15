import spotipy


class User:
    def __init__(self, username: str, client: spotipy.Spotify):
        self.username = username
        self.client = client

    def get_user(self):
        return self.client.user(self.username)

    def get_users_playlists(self):
        return self.client.user_playlists(self.username)

    def play_next_track(self):
        self.client.next_track()

    def play_previous_track(self):
        self.client.previous_track()

    def create_playlist(
        self, playlist_name: str, description: str = None, public: bool = True
    ):
        self.client.user_playlist_create(
            self.username, playlist_name, public=public, description=description
        )
