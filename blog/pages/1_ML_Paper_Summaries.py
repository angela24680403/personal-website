import streamlit as st
from pathlib import Path

st.title("📚 ML Paper Summaries")

posts_path = Path("blog/paper_summaries")
for post_file in posts_path.glob("*.md"):
    title = post_file.stem.split("_", 1)[-1].replace("-", " ").title()
    print(title)
    content = post_file.read_text(encoding="utf-8")
    with st.expander(title):
        st.markdown(content)
