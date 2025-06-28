def get_emotion_level(emotion):
    return {
        "Calm": 1,
        "Frustrated": 5,
        "Curious": 3
    }.get(emotion, 1)