# main.py

from emotion_detector import detect_emotion
from voice_modulator import get_voice_parameters
from tts_engine import speak_text


if __name__ == "__main__":

    print("Empathy Engine Started")
    print("Type a sentence to speak with emotion")
    print("Type 'exit' to stop\n")

    while True:

        # take input
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("Program terminated.")
            break

        # detect emotion
        emotion,score = detect_emotion(text)

        print(f"Detected Emotion: {emotion} (confidence: {score:.2f})")

        # get voice parameters
        params = get_voice_parameters(emotion,score)

        rate = params["rate"]
        volume = params["volume"]
        print(f"Voice Rate: {rate}, Volume: {volume}")
        # speak text
        speak_text(text, rate, volume)