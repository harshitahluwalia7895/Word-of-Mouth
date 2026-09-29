from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Packt Workshops — I'm Attending",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      .stApp { background: #050816; }
      .block-container { max-width: 1500px; padding: 0; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("card_generator.html").read_text(encoding="utf-8")
components.html(html, height=1120, scrolling=True)
