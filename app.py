import streamlit as st

st.set_page_config(layout="wide")

# Remove padding & margin
st.markdown("""
    <style>
        .block-container {
            padding: 0rem;
        }
        iframe {
            width: 100% !important;
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

# Hide Streamlit UI
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load HTML
with open("start.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1000, scrolling=True)
