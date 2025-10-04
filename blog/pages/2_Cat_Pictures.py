import streamlit as st
from pathlib import Path
from PIL import Image

st.title("🐱 My Cat Gallery")
st.write("If you'd like some break from reading awesome LLM blog posts, here are some cute pictures!")
# Path to the cat images folder
cat_folder = Path(__file__).parent.parent / "cats"

if not cat_folder.exists():
    st.error("No cat images found. Make sure the 'cats' folder exists.")
else:
    cat_images = list(cat_folder.glob("*.[jp][pn]g"))  # jpg and png
    if not cat_images:
        st.info("No cat images found in the folder.")
    else:
        for img_path in cat_images:
            image = Image.open(img_path)
            st.image(image, caption=img_path.stem, use_container_width=True)
