import streamlit as st
from pathlib import Path

st.title("📚 ML Study Notes")

posts_path = Path("blog/study_notes")
for post_file in posts_path.glob("*.md"):
    title = post_file.stem.split("_", 1)[-1].replace("-", " ")
    content = post_file.read_text(encoding="utf-8")
    with st.expander(title):
        st.markdown(content)
