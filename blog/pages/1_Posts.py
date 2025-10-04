import streamlit as st
from pathlib import Path

st.title("📚 Blog Posts")

posts_path = Path("blog/posts")
for post_file in posts_path.glob("*.md"):
    title = post_file.stem.replace("-", " ").title()
    content = post_file.read_text(encoding="utf-8")
    with st.expander(title):
        st.markdown(content)
