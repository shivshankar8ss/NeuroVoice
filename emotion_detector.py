from transformers import pipeline

# Load pre-trained emotion detection model
# This model can detect emotions like joy, sadness, anger, fear, surprise, neutral
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

def map_emotion(model_emotion):
    """
    Map model emotion to project emotion categories
    """

    mapping = {
        "joy": "happy",
        "surprise": "happy",
        "sadness": "sad",
        "anger": "angry",
        "fear": "anxious",
        "disgust": "angry",
        "neutral": "neutral"
    }

    return mapping.get(model_emotion, "neutral")


def detect_emotion(text):
    """
    Detect emotion and return mapped emotion + confidence
    """

    result = emotion_classifier(text)

    model_emotion = result[0]['label']
    score = result[0]['score']

    mapped_emotion = map_emotion(model_emotion)

    return mapped_emotion, score

# Simple test
if __name__ == "__main__":

    print("Emotion Detection Started")
    print("Type a sentence to detect emotion.")
    print("Type 'exit' to stop the program.\n")

    while True:
        # take user input
        text = input("Enter a sentence: ")

        # termination condition
        if text.lower() == "exit":
            print("Program terminated.")
            break

        # detect emotion
        emotion = detect_emotion(text)

        # print result
        print(f"Detected Emotion: {emotion}\n")