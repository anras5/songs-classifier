import streamlit as st
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
        st.write(SpotipyHandler.search_song(song_name_input))

