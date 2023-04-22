import pandas as pd
import streamlit as st

from utils import query
from viz import plot_song_themes

st.set_page_config(
    page_title="Song Lyrics Analysis", initial_sidebar_state="collapsed"
)

st.title("Classify Song Theme")

st.markdown(
    """This application allows you to classify the theme of a song lyrics into: sad, good-vibes, or aggressive
"""
)

txt = st.text_area('Text to analyze', "", height=300)

if st.button("Classify") and txt != "":
    output = query({
        "inputs": txt,
    })
    df = pd.DataFrame(output[0])
    theme_plot = plot_song_themes(df)
    st.pyplot(theme_plot)
