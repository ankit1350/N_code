import time
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Speed of speech

# Song lyrics as a list of lines
lyrics = [
    "What I feel for you is so much more than I can say",
    "No one compares to what you are",
    "I know I knew it from the start",
    "Promise me my love, don't take another heart",
    "I've been hurt before I wanna new start",
    "No I know that you're not my first love",
    "But I know that from today",
    "We can say history, stays history and you will always love me"
]

# Delay (in seconds) between lines
delay = 3

# Start singing
for line in lyrics:
    print(line)
    engine.say(line)
    engine.runAndWait()
    time.sleep(delay)
