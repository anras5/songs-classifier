import pandas as pd
import spotipy.exceptions
import streamlit as st

from classifier_handler import ClassifierHandler
from spotipy_handler import SpotipyHandler

st.title("Songs Classifier App :headphones: :notes:")
st.markdown("**Search for your favorite song and discover to what genre it belongs!**")

with st.form(key="songs_form"):
    song_name_input = st.text_input("Song name:", placeholder="Your favorite song...")
    submit_button = st.form_submit_button("Search")

if submit_button:
    if song_name_input == "":
        st.write("**Song name cannot be empty!**")
    else:
        try:
            song = SpotipyHandler.search_song(song_name_input)
            predicted_class = ClassifierHandler.send_request(song)

            col1, col2 = st.columns(2)

            # basic data about the song
            with col1:
                if song.album_photo is not None:
                    st.image(song.album_photo, width=200)
                st.header(song.name)
                st.markdown(f"{song.artist}, {song.album_name}")

            with col2:

                class_settings = {
                    'pop/dance': ('green', ':cd:'),
                    'rock': ('red', ':guitar:'),
                    'chill/relax': ('blue', ':person_in_lotus_position:'),
                    'classical': ('orange', ':violin:')
                }
                st.write(f"Predicted class: :{class_settings[predicted_class][0]}[{predicted_class}] {class_settings[predicted_class][1]}")
                if song.audio_preview is not None:
                    st.write(":headphones: Here is a sample of the song:")
                    st.audio(song.audio_preview)
                else:
                    st.write("Sorry, sample for this song is not available :cry:")

            # plotting the song features
            st.divider()
            st.write("Data for your song:")
            df = pd.DataFrame({
                'popularity': [song.features.popularity],
                'duration_ms': [song.features.duration_ms],
                'explicit': [song.features.explicit],
                'danceability': [song.features.danceability],
                'energy': [song.features.energy],
                'loudness': [song.features.loudness],
                'mode': [song.features.mode],
                'speechiness': [song.features.speechiness],
                'acousticness': [song.features.acousticness],
                'instrumentalness': [song.features.instrumentalness],
                'valence': [song.features.valence],
                'tempo': [song.features.tempo],
            }, index=['Song'])
            st.dataframe(df)
        except spotipy.exceptions.SpotifyException:
            st.toast('Error!', icon="🚨")
            st.markdown("Sorry, there was an error getting your song from Spotify :cry:")
