import pyaudio


# Microphone configuration
AUDIO = pyaudio.PyAudio()
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1280  # How much audio (in number of samples) to predict on at once
SAMPLE_RATE = 22050

# Configuring the voice
MODEL_NAME = "tts_models/de/css10/vits-neon"

# Wake word detection settings
DEBOUNCE_TIME = 2.0  # Prevent the same word being detected multiple times
THRESHOLD = {"alexa": 0.5}  # Is needed to be able to use the debounce_time


# Speech recognition settings
RECOGNITION_TIMEOUT = 5  # seconds
