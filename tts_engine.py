# tts_engine.py

import pyttsx3
import os

audio_counter = 1

def speak_text(text, rate, volume):
    """
    Convert text to speech with given parameters
    """
    global audio_counter
    # Initialize engine each time (important for loops)
    engine = pyttsx3.init()

    # set speaking speed
    engine.setProperty('rate', rate)

    # set volume (0.0 to 1.0)
    engine.setProperty('volume', volume)

    os.makedirs("audio_outputs", exist_ok=True)
    filename = f"audio_outputs/output_{audio_counter}.wav"
    # Save audio to file
    engine.save_to_file(text, filename)

    # speak text
    engine.say(text)

    # execute speech
    engine.runAndWait()

    # stop engine to release resources
    engine.stop()
    print(f"Audio saved as: {filename}")
    audio_counter+=1
    return filename

