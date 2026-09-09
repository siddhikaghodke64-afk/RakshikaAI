# 🛡️ Rakshika AI – Smart Women Safety System

**Rakshika AI** is an AI-powered smart women safety system designed to detect potential threats in real time and assist users during emergency situations.

The system uses **YOLO-based computer vision** to detect potentially dangerous objects and combines the detection results with a **risk assessment engine** to identify high-risk situations. It also provides features such as **SOS alerts, emergency contacts, live location support, incident history, and automated evidence logging**.

---

## 🎯 Problem Statement

Personal safety is a major concern, especially in situations where immediate assistance may not be available.

Traditional safety systems often depend on the user manually triggering an emergency alert. Rakshika AI aims to provide an additional **AI-assisted layer of safety** by continuously analyzing visual input and identifying potentially dangerous situations.

---

## 💡 Our Solution

Rakshika AI combines **Artificial Intelligence, Computer Vision, and Emergency Response** into one system.

```text
Camera / Video
      ↓
Image Processing
      ↓
YOLO Object Detection
      ↓
Threat Identification
      ↓
Risk Score Calculation
      ↓
Risk Assessment
      ↓
Alert / SOS
      ↓
Emergency Response
      ↓
Incident History
```

---

## 🚀 Key Features

### 🔍 Real-Time Threat Detection

Uses YOLO-based object detection to identify potentially dangerous objects from camera input.

### ⚠️ AI-Based Risk Assessment

Each detected object is assigned a risk score. The system uses these scores to determine the severity of a situation.

### 🚨 SOS Emergency System

Provides an SOS mechanism that can be used during emergency situations.

### 📍 Live Location Support

Location information can be used to help emergency contacts identify the user's location.

### 👥 Emergency Contacts

Allows important emergency contacts to be maintained for quick access during an emergency.

### 📋 Incident History

Detected incidents can be recorded and reviewed later.

### 📸 Evidence Logging

The system can save screenshots of relevant detections for incident records.

### 🌐 Web-Based Interface

A Flask-based interface provides a simple way to interact with the safety system.

---

## 🧠 AI Detection

Rakshika AI uses **YOLO (You Only Look Once)** for real-time object detection.

Example objects considered by the risk engine include:

| Object       | Example Risk Score |
| ------------ | -----------------: |
| Person       |                  5 |
| Knife        |                 70 |
| Baseball Bat |                 40 |
| Scissors     |                 30 |
| Backpack     |                  5 |
| Car          |                 10 |
| Truck        |                 15 |

> Risk scores are configurable and are intended for prototype/demo purposes.

---

## 🛠️ Technologies Used

| Technology              | Purpose                   |
| ----------------------- | ------------------------- |
| **Python**              | Core development          |
| **YOLO / Ultralytics**  | Object detection          |
| **OpenCV**              | Image & video processing  |
| **Flask**               | Web application           |
| **SQLite**              | Data storage              |
| **HTML/CSS/JavaScript** | User interface            |
| **CSV / JSON**          | Logging and system status |

---

## 📂 Project Structure

```text
Rakshika-AI/
│
├── app.py
├── logger.py
├── detection.py
│
├── models/
│   └── YOLO models
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── database/
│   └── safety.db
│
├── screenshots/
│
├── requirements.txt
├── .gitignore
└── README.md
```

> Update the structure according to your actual project files before publishing.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Rakshika-AI.git
cd Rakshika-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` yet:

```bash
pip install ultralytics opencv-python flask
```

---

## ▶️ Running the Project

Start the Flask application:

```bash
python app.py
```

Then open the local application in your browser:

```text
http://127.0.0.1:5000
```

---

## 🔐 Risk Assessment Engine

Rakshika AI uses configurable risk scores to prioritize potentially dangerous detections.

Example:

```python
RISK_SCORES = {
    "person": 5,
    "knife": 70,
    "baseball bat": 40,
    "scissors": 30,
    "backpack": 5,
    "car": 10,
    "truck": 15
}
```

The calculated risk level can be used by the application to determine when an alert should be generated.

---

## 🌟 Why Rakshika AI?

Traditional emergency systems often require the user to manually recognize a threat and trigger an alert.

Rakshika AI aims to provide an **AI-assisted approach** by:

* Monitoring visual input
* Detecting potential threats
* Calculating a risk level
* Recording incidents
* Supporting SOS functionality
* Providing emergency information

This creates an additional intelligent layer between **threat detection and emergency response**.

---

## 🎯 Applications

Rakshika AI can be adapted for:

* 👩 Women safety
* 🏫 College and campus security
* 🏙️ Public-space monitoring
* 🏢 Workplace safety
* 🚨 Emergency response
* 📹 Smart surveillance
* 🤖 AI-based security systems

---

## 🔮 Future Scope

Future improvements may include:

* 📱 Android/mobile application
* 🗺️ Advanced real-time location tracking
* ☁️ Cloud-based incident storage
* 📞 Automated emergency calling
* 🔔 SMS/notification integration
* 🧠 Improved threat classification
* 👥 Crowd behavior analysis
* 📹 Multi-camera monitoring
* 🔊 Voice-based emergency activation
* 🤖 Improved AI-based risk prediction

---

## 👩‍💻 Project Information

**Project Name:** Rakshika AI
**Project Type:** AI & Computer Vision Safety System
**Domain:** Artificial Intelligence & Machine Learning
**Institution:** Sanjivani University

---

## ⚠️ Disclaimer

Rakshika AI is an academic/prototype project developed to demonstrate the application of artificial intelligence and computer vision in safety systems.

AI-based detection can produce incorrect results. The system should therefore be treated as an **assistive prototype** and not as a replacement for professional emergency or security services.

---

## ⭐ Support

If you find **Rakshika AI** interesting, consider giving the repository a ⭐ on GitHub.

**Built with Python, Computer Vision, and AI for a safer future. 🛡️**
