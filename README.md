# 🎙️ Empathy Engine – Emotion-Aware Text-to-Speech System

An AI-powered system that analyzes the emotional tone of text and generates speech with appropriate vocal modulation. The project detects emotions from input text and adjusts speech characteristics such as **rate** and **volume** to simulate human-like emotional expression.

This project demonstrates integration of **Natural Language Processing**, **Machine Learning**, and **Speech Synthesis** into a single application with a simple **web interface**.

---

## 🚀 Features

- Emotion detection from input text using a **Transformer-based NLP model**
- Supports multiple emotions such as:
  - Joy
  - Sadness
  - Anger
  - Fear
  - Surprise
  - Neutral
- **Emotion intensity scaling** using confidence scores
- **Voice modulation** based on detected emotion:
  - Speech Rate
  - Volume
- Generates **playable audio files**
- Built with **FastAPI backend**
- Simple **web UI for interaction**
- Audio playback directly in the browser

---

## 🧠 How It Works

The system follows this pipeline:

```text
empathy-engine
│
├── app.py                     # FastAPI application for the web interface
├── main.py                    # CLI version of the Empathy Engine
│
├── emotion_detector.py        # Detects emotion from input text using transformer model
├── voice_modulator.py         # Maps detected emotion to speech parameters
├── tts_engine.py              # Generates speech and saves audio files
│
├── templates                  # HTML templates for the web UI
│   └── index.html             # Main UI page
│
├── audio_outputs              # Stores generated audio files
│   ├── output_1.wav
│   ├── output_2.wav
│   └── ...
│
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation

```

---

## 🛠 Technologies Used

- **Python**
- **FastAPI** – Web framework
- **HuggingFace Transformers** – Emotion detection model
- **PyTorch** – ML backend
- **pyttsx3** – Text-to-speech engine
- **Jinja2** – HTML templating
- **Uvicorn** – ASGI server

---


## 👨‍💻 Developed By

**Shivshankar Kumar**

Mechatronics and Automation Engineering  
IIIT Bhagalpur

---

