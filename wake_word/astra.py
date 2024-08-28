import pyaudio
import time
import logging
import numpy as np
import speech_recognition as sr
from openwakeword.model import Model
from typing import Dict, List, Union
from utils.settings.audio_settings import (
    FORMAT,
    CHANNELS,
    RATE,
    CHUNK,
    SAMPLE_RATE,
    AUDIO,
    DEBOUNCE_TIME,
    THRESHOLD,
    RECOGNITION_TIMEOUT,
)
from utils.settings.assistant_settings import ASSISTANTS
from assistant.abstract_assistant import AbstractAssistant
from LLM.classification_llm import CLASSIFICATION_LLM

logger = logging.getLogger("Astra")


class Astra:

    def __init__(self) -> None:
        # Wake word detection variables
        self.model = Model(wakeword_models=["alexa"])
        self.wake_words: List[str] = ["alexa"]

        # Assistant variables
        self.assistants: Dict[str, AbstractAssistant] = ASSISTANTS
        self.classification_llm = CLASSIFICATION_LLM()

        # Audio variables
        self.audio = pyaudio.PyAudio()
        self.mic_stream = AUDIO.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone(sample_rate=SAMPLE_RATE, chunk_size=CHUNK)

    def listen_to_wake_word(self) -> None:
        audio = np.frombuffer(self.mic_stream.read(CHUNK), dtype=np.int16)

        prediction = self.model.predict(
            audio,
            threshold=THRESHOLD,
            debounce_time=DEBOUNCE_TIME,
        )
        for wake_word in self.wake_words:
            score = prediction[wake_word]
            is_wake_word_detected = score > 0.5
            if is_wake_word_detected:
                logger.info(f"Wake word '{wake_word}' detected")
                speech = self.listen_to_speech()
                assistant_id = self.determine_assistant(speech)
                assistant = self.assistants.get(assistant_id, None)
                if assistant:
                    assistant.respond(speech)
                logger.info("Listen for wake words...")

    def listen_to_speech(self) -> Union[str, None]:
        speech = None

        logger.info("Listen to speech...")
        start_time = time.time()
        with self.mic as source:
            try:
                audio = self.recognizer.listen(source, timeout=RECOGNITION_TIMEOUT)

            except sr.WaitTimeoutError:
                logger.warning("Timeout while waiting for speech...")
                logger.debug(f"End time: {time.time() - start_time}")
                return None

            try:
                speech = self.recognizer.recognize_google(audio, language="de-DE")
            except sr.UnknownValueError:
                logger.error("Could not understand audio")
                return None
        logger.debug(f"Detected speech: {speech} ")

        return speech

    def determine_assistant(self, speech: str) -> str:
        assistant = self.classification_llm.process(speech=speech)
        logger.debug(f"Selected assistant: {assistant}")
        return assistant
