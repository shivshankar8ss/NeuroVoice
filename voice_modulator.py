def get_voice_parameters(emotion, confidence):

    emotion = emotion.lower()

    intensity = confidence

    rate = 160
    volume = 0.9

    if emotion == "happy":
        rate = 170 + int(30 * intensity)
        volume = min(1.0, 0.8 + (0.2 * intensity))

    elif emotion == "sad":
        rate = 140 - int(20 * intensity)
        volume = max(0.5, 0.8 - (0.3 * intensity))

    elif emotion == "angry":
        rate = 180 + int(40 * intensity)
        volume = min(1.0, 0.9 + (0.1 * intensity))

    elif emotion == "anxious":
        rate = 150 - int(10 * intensity)
        volume = 0.8

    else:  # neutral
        rate = 160
        volume = 0.9

    return {
        "rate": rate,
        "volume": volume
    }