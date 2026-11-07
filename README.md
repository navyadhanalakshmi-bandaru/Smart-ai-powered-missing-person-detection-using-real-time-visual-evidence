
# 🔍 AI-Powered Missing Person Finder

An **AI System for Missing Persons Identification** built using **Streamlit**, **OpenCV**, and **SQLite**.  
This project leverages **facial recognition** to help identify and locate missing persons through image comparison and public sighting reports.

---

## 🧠 Project Overview

Thousands of people go missing every year, and timely identification plays a crucial role in reuniting them with their families.  
This project assists **law enforcement agencies** and **NGOs** using **AI-based facial recognition** to:

- 🧍 Detect and register missing persons  
- 📸 Compare uploaded images using face recognition  
- 🕵️ Identify possible matches with similarity scores  
- 📱 Allow the public to report sightings with photos  
- 🧾 Maintain case data using an easy-to-use database system  

---

## ⚙️ Technologies Used

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | Web interface for admin and public dashboards |
| **OpenCV** | Image processing and face detection |
| **NumPy** | Numerical computation for embeddings |
| **SQLite** | Lightweight database for storing cases and sightings |
| **Pillow** | Image handling library |
| **MediaPipe / OpenCV** | Used for extracting and comparing facial features |

---

## 🗂️ Project Structure

missing_person_finder/
├── app.py # Admin dashboard (register, search, manage cases)
├── mobile_app.py # Public reporting portal
├── database.py # Database setup and connection
├── face_utils.py # Face recognition and comparison logic
├── requirements.txt # All required dependencies
├── README.md # Project documentation
└── resources/
├── images/ # Stored images of missing persons
└── temp/ # Temporary images from uploads



---

## 🚀 How to Run the Project

### 🧩 1. Clone the repository
```bash
https://github.com/navyadhanalakshmi-bandaru/Smart-ai-powered-missing-person-detection-using-real-time-visual-evidence.git
cd missing_person_finder

### 🧩 2. Create a virtual environment
```bash
python -m venv env
env\Scripts\activate     # On Windows

###🧩 3. Install dependencies
pip install -r requirements.txt
###🧩 4. Initialize the database
python database.py
##✅ You should see:

Database initialized successfully!
###🧩 5. Run the main admin app
streamlit run app.py

###🧩 6. Run the public (mobile) app
streamlit run mobile_app.py
🧰 Features
✅ Admin Dashboard


Register new missing persons


Upload photo, details, and last seen info


Search database using face recognition


Manage sightings and update case status


✅ Public Portal


Upload a photo of a sighted person


Enter location and description


AI automatically compares against the database


Matches shown with confidence percentage


✅ Database


Stores missing persons, sightings, and user accounts


Uses SQLite for simplicity and portability



📊 Example Outputs
🔍 Admin Search


Uploaded Image: rohittest.jpg


Top Matches:


Rohit — Similarity: 95%


Dhoni — Similarity: 84%




📱 Public Sighting


Location: Guntur


Description: Seen near temple


Match Found: Rohit (Confidence: 0.95)



🎯 Objective
The goal of this project is to speed up missing person identification using modern AI and face recognition tools.
It can be used by:


🕵️ Police departments


🧒 NGOs and Child Welfare Organizations


🧑‍💻 AI researchers and developers



🧩 Future Enhancements


🌟 Use FaceNet or DeepFace for more accurate recognition


☁️ Add cloud storage for large-scale deployment


📷 Real-time CCTV camera integration


📊 Visual analytics dashboard for authorities



💖 Acknowledgements
Special thanks to:


MediaPipe and OpenCV teams for open-source computer vision tools


Streamlit community for enabling quick, interactive AI apps


Volunteers and NGOs for real-world inspiration



👩‍💻 Author
Developed by: @Veena3028
💬 “Technology for Humanity — Using AI to reunite families.”

📜 License
This project is open-source and available under the MIT License.

⭐ If you like this project, please star the repository on GitHub!


