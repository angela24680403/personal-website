import streamlit as st

st.set_page_config(page_title="My Blog", page_icon="📝")

st.title("✨ Welcome to Angie's Website!")
st.write("I am a Microsoft Applied Scientist/UCL MEng excited to learn more aboout LLM Reasoning, Explainable AI and Mechanistic Interperatability. I can't wait to be sharing some of my recent readings and experiments here.")

# Load CSS
def load_css(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("blog/static/style.css")
