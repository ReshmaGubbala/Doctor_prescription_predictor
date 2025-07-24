import streamlit as st
from ocr import extract_text_google
from translate import translate_text_google
import os

# Set your service account key file here
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

st.set_page_config(page_title="Multilingual Prescription Reader", layout="centered")
st.title("🩺 Multilingual Handwritten Prescription Recognition")

# File uploader
uploaded_file = st.file_uploader("📤 Upload a handwritten prescription (Hindi, Telugu, etc.)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="🖼 Uploaded Image", use_column_width=True)

    # Read image bytes
    image_bytes = uploaded_file.read()

    with st.spinner("🔍 Extracting handwritten text..."):
        extracted_text = extract_text_google(image_bytes)
    st.subheader("📜 Extracted Text:")
    st.code(extracted_text)

    with st.spinner("🌐 Translating to English..."):
        translated = translate_text_google(extracted_text)
    st.subheader("🗣 Translated Text:")
    st.success(translated)
