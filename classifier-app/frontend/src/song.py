from dataclasses import dataclass


@dataclass
class SongFeatures:
    popularity: int
    duration_ms: int
    explicit: bool
    danceability: float
    energy: float
    loudness: float
    mode: bool
    speechiness: float
    acousticness: float
    instrumentalness: float
    valence: float
    tempo: float


@dataclass
class Song:
    id: str
    name: str
    artist: str
    album_name: str = "No album"
    album_photo: str = None
    audio_preview: str = None
    features: SongFeatures = None
