import re
import logging
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


logger = logging.getLogger("AbstractAssistant")


class AbstractAssistant(ABC):
    def __init__(self) -> None:
        self.tts_engine = TTS(model_name=MODEL_NAME)
        self.assistant_id = None

    @abstractmethod
    def respond(self, speech: Optional[str] = "") -> None:
        pass  # Implement this method in subclasses to handle the response to speech

    def sanitize_text(self, text: str) -> str:
        """
        Removes all special characters from the text.
        This is required as the TTS engine can't handle special characters well
        1. Remove non-alphanumeric characters except spaces
        2. Replace multiple spaces with a single space
        """
        sanitized_text = re.sub(r"\W+_", " ", text)
        sanitized_text = re.sub(r"\s+", " ", sanitized_text).strip()
        return sanitized_text

    def say(self, text: str) -> None:
        text = self.sanitize_text(text)
        logger.debug(f"Playing audio for response: {text}")
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
            logger.exception(f"Exception playing audio: {str(e)}")
