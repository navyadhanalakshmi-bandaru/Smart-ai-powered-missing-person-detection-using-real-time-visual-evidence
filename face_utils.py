import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def extract_face_encoding(image_path):
    """Detects a face and returns a normalized 1D encoding"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    (x, y, w, h) = faces[0]
    face = cv2.resize(gray[y:y+h, x:x+w], (100, 100))
    encoding = face.flatten() / 255.0  # normalize pixel values
    return encoding.astype(np.float32)

def compare_faces(enc1, enc2):
    """Compare two encodings with cosine similarity"""
    if enc1 is None or enc2 is None:
        return 0.0
    enc1, enc2 = enc1.flatten(), enc2.flatten()
    dot = np.dot(enc1, enc2)
    norm = np.linalg.norm(enc1) * np.linalg.norm(enc2)
    return float(dot / norm)

def save_uploaded_image(uploaded_file, directory="resources/temp"):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return path
