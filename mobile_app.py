import streamlit as st
import numpy as np
import os
from database import get_connection
from face_utils import extract_face_encoding, compare_faces, save_uploaded_image

st.set_page_config(page_title="Report Sighting", layout="centered")
st.title("📱 Report Sighting - Missing Person Finder")

image = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
location = st.text_input("📍 Location Seen")
desc = st.text_area("📝 Description")

if st.button("Search & Report") and image and location:
    path = save_uploaded_image(image, "resources/temp")
    enc = extract_face_encoding(path)
    conn = get_connection()
    persons = conn.execute("SELECT name, image_path, face_encoding FROM missing_persons").fetchall()
    conn.close()

    best_match, best_score = None, 0.0
    for name, img, enc_blob in persons:
        db_enc = np.frombuffer(enc_blob, dtype=np.float32)
        sim = compare_faces(enc, db_enc)
        if sim > best_score:
            best_match, best_score = (name, img), sim

    if best_match and best_score > 0.75:
        st.success(f"Possible match found: {best_match[0]} ({best_score:.2f})")
        st.image(best_match[1])
    else:
        st.warning("No match found.")
