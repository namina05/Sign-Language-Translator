<h1 align="center">🤟 Sign Vision AI</h1>

<p align="center">
  Real-Time Sign Language Translation using Computer Vision and Machine Learning
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-Frontend-61DAFB?logo=react">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-FF6F00">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikitlearn">
</p>

---

## 📖 Overview

Sign Vision AI is a real-time sign language translation system that uses a webcam feed to recognize hand gestures and convert them into text.

The application combines:

- 🎥 OpenCV for camera capture
- ✋ MediaPipe for hand landmark detection
- 🤖 Scikit-Learn for gesture classification
- ⚡ FastAPI for backend APIs and video streaming
- ⚛️ React for the user interface

---

## ✨ Features

<ul>
  <li>Real-time webcam streaming</li>
  <li>Live hand detection</li>
  <li>Gesture recognition using Machine Learning</li>
  <li>Prediction confidence score</li>
  <li>Sentence buffer</li>
  <li>Modern React dashboard</li>
  <li>Automatic camera start/stop</li>
</ul>

---

## 🏗️ System Architecture

```text
Camera
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Feature Extraction
   ↓
Random Forest Classifier
   ↓
Prediction + Confidence
   ↓
FastAPI Backend
   ↓
React Frontend
```

---

## 🖥️ Application Screens

### 🏠 Home Page

- Project overview
- Performance statistics
- Quick access to translator

### 🤟 Translator Page

- Live camera feed
- Current prediction
- Confidence score
- Hand status
- Sentence buffer

---

## 📊 Model Details

<table>
<tr>
<th>Property</th>
<th>Value</th>
</tr>

<tr>
<td>Algorithm</td>
<td>Random Forest Classifier</td>
</tr>

<tr>
<td>Accuracy</td>
<td>99.06%</td>
</tr>

<tr>
<td>Supported Classes</td>
<td>26 ASL Letters</td>
</tr>

<tr>
<td>Dataset Size</td>
<td>5000+ Samples</td>
</tr>

</table>

---

## 🛠️ Tech Stack

<table>
<tr>
<th>Category</th>
<th>Technology</th>
</tr>

<tr>
<td>Frontend</td>
<td>React, Vite, React Router</td>
</tr>

<tr>
<td>Backend</td>
<td>FastAPI</td>
</tr>

<tr>
<td>Computer Vision</td>
<td>OpenCV, MediaPipe</td>
</tr>

<tr>
<td>Machine Learning</td>
<td>Scikit-Learn</td>
</tr>

<tr>
<td>Language</td>
<td>Python, JavaScript</td>
</tr>

</table>

---

## 📂 Project Structure

```text
sign_language_translator/
│
├── app/
│   ├── api.py
│   ├── main.py
│   ├── predictions.py
│   └── sharedframe.py
│
├── core/
│   ├── camera.py
│   ├── hand_tracker.py
│   ├── gesture_recognizer.py
│   └── gesture_smoother.py
│
├── models/
│   └── classifier.pkl
│
├── services/
│   └── dataset_collector.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/namina05/Sign-Language-Translator.git
cd Sign-Language-Translator
```

### Backend Setup

```bash
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend
npm install
```

---

## ▶️ Run Application

### Development

```bash
python -m uvicorn app.api:app --reload
```

Frontend:

```bash
cd frontend
npm run dev
```

### Production

Build React:

```bash
cd frontend
npm run build
```

Run FastAPI:

```bash
python -m uvicorn app.api:app
```

---

## 🎯 Future Improvements

- Word prediction
- Sentence generation
- Text-to-Speech
- Dynamic gesture recognition
- Model retraining interface
- Cloud deployment

---

<p align="center">
  Made with ❤️ using React, FastAPI, OpenCV and MediaPipe
</p>