import os

import httpx
from dotenv import load_dotenv

from song import Song

load_dotenv("/app/.env")


class ClassifierHandler:

    @classmethod
    def send_request(cls, song: Song):
        r = httpx.post(os.getenv("CLASSIFIER_URL"), json={
            "dataframe_split": {
                "columns": ["popularity", "duration_ms", "explicit", "danceability", "energy", "loudness",
                            "mode", "speechiness", "acousticness", "instrumentalness", "valence", "tempo"],
                "data": [[
                    song.features.popularity,
                    song.features.duration_ms,
                    song.features.explicit,
                    song.features.danceability,
                    song.features.energy,
                    song.features.loudness,
                    song.features.mode,
                    song.features.speechiness,
                    song.features.acousticness,
                    song.features.instrumentalness,
                    song.features.valence,
                    song.features.tempo,
                ]]
            }
        })
        return r.json()['predictions'][0]
