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
## ▶️ How to Run the Project

Follow these steps to run the Empathy Engine locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/empathy-engine.git
cd empathy-engine
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Web Application

```bash
uvicorn app:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

Enter text in the UI and click **Generate Speech** to detect emotion and hear the generated audio.

---

### 5. Run the CLI Version (Optional)

```bash
python main.py
```

Enter text directly in the terminal to generate emotionally modulated speech.

---

### 6. Output

Generated audio files will be stored in:

```
audio_outputs/
```

Example:

```
audio_outputs/output_1.wav
audio_outputs/output_2.wav
```


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

