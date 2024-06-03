import os
from song import Song, SongFeatures

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv("/app/.env")

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET')
    )
)


class SpotipyHandler:

    @classmethod
    def search_song(cls, song_name: str) -> Song:
        search_result = sp.search(song_name, type='track')['tracks']['items'][0]
        song = Song(
            id=search_result['id'],
            name=search_result['name'],
            artist=search_result['album']['artists'][0]['name'],
            album_name=search_result['album']['name'],
            album_photo=search_result['album']['images'][0]['url']
        )
        song_features = sp.audio_features(song.id)[0]
        song.features = SongFeatures(
            popularity=search_result['popularity'],
            duration_ms=song_features['duration_ms'],
            explicit=search_result['explicit'],
            danceability=song_features['danceability'],
            energy=song_features['energy'],
            loudness=song_features['loudness'],
            mode=song_features['mode'],
            speechiness=song_features['speechiness'],
            acousticness=song_features['acousticness'],
            instrumentalness=song_features['instrumentalness'],
            valence=song_features['valence'],
            tempo=song_features['tempo']
        )

        return song
