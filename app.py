import streamlit as st
import numpy as np
import os
from database import get_connection, init_database
from face_utils import extract_face_encoding, compare_faces, save_uploaded_image

st.set_page_config(page_title="Missing Person Finder", layout="wide")
st.title("🔍 Missing Person Finder (Admin Portal)")

init_database()

menu = ["Register Missing Person", "Search Database"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Register Missing Person":
    st.header("🧍 Register New Missing Person")
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    location = st.text_input("Last Seen Location")
    contact = st.text_input("Contact Number")
    desc = st.text_area("Description")
    image = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

    if st.button("Save") and name and image:
        path = save_uploaded_image(image, "resources/images")
        encoding = extract_face_encoding(path)
        if encoding is None:
            st.error("No face detected in this image.")
        else:
            conn = get_connection()
            conn.execute('INSERT INTO missing_persons (name, age, gender, last_seen_location, contact_number, description, image_path, face_encoding) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                         (name, age, gender, location, contact, desc, path, encoding.tobytes()))
            conn.commit()
            conn.close()
            st.success(f"{name} registered successfully!")
            st.balloons()

elif choice == "Search Database":
    st.header("🔎 Search Missing Person")
    image = st.file_uploader("Upload Image to Search", type=["jpg", "jpeg", "png"])
    if st.button("Search") and image:
        query_path = save_uploaded_image(image)
        query_enc = extract_face_encoding(query_path)
        conn = get_connection()
        data = conn.execute("SELECT name, image_path, face_encoding FROM missing_persons").fetchall()
        conn.close()

        results = []
        for name, img_path, enc_blob in data:
            db_enc = np.frombuffer(enc_blob, dtype=np.float32)
            sim = compare_faces(query_enc, db_enc)
            results.append((name, img_path, sim))

        results.sort(key=lambda x: x[2], reverse=True)
        if results:
            st.subheader("Top Matches:")
            for n, img, s in results[:3]:
                st.write(f"**{n}** — Similarity: {s:.2f}")
                st.image(img, width=200)
        else:
            st.warning("No matches found.")
