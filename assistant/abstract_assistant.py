import numpy as np
from TTS.api import TTS
from abc import ABC, abstractmethod
from typing import Optional

from utils.settings.audio_settings import (
    MODEL_NAME,
    AUDIO,
    FORMAT,
    CHANNELS,
    SAMPLE_RATE,
)


class AbstractAssistant(ABC):
    def __init__(self) -> None:
        self.tts_engine = TTS(model_name=MODEL_NAME)
        self.assistant_id = None

    @abstractmethod
    def respond(self, speech: Optional[str] = "") -> None:
        pass  # Implement this method in subclasses to handle the response to speech

    def say(self, text: str) -> None:
        wav = np.array(self.tts_engine.tts(text))
        self.play_audio(wav)

    def play_audio(self, audio_data: np.ndarray) -> bool:
        try:
            stream = AUDIO.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=SAMPLE_RATE,
                output=True,
            )
            # Convert numpy array to bytes
            audio_data = (audio_data * 32767).astype(np.int16)  # Scale to 16-bit PCM
            audio_bytes = audio_data.tobytes()
            stream.write(audio_bytes)
        except Exception as e:
            print(f"Error playing audio: {e}")
