# app.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from emotion_detector import detect_emotion
from voice_modulator import get_voice_parameters
from tts_engine import speak_text

import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/audio_outputs", StaticFiles(directory="audio_outputs"), name="audio")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process", response_class=HTMLResponse)
def process_text(request: Request, text: str = Form(...)):

    emotion, score = detect_emotion(text)

    params = get_voice_parameters(emotion, score)

    rate = params["rate"]
    volume = params["volume"]

    # generate speech and get filename
    audio_file = speak_text(text, rate, volume)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "emotion": emotion,
            "confidence": f"{score:.2f}",
            "audio_file": audio_file
        }
    )

    emotion, score = detect_emotion(text)

    params = get_voice_parameters(emotion, score)

    rate = params["rate"]
    volume = params["volume"]

    # generate speech
    speak_text(text, rate, volume)

    audio_file = speak_text(text, rate, volume)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "emotion": emotion,
            "confidence": f"{score:.2f}",
            "audio_file": audio_file
        }
    )