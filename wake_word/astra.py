import pyaudio
import numpy as np
import speech_recognition as sr
from openwakeword.model import Model
from typing import Dict, List, Union
from utils.settings.audio_settings import (
    FORMAT,
    CHANNELS,
    RATE,
    CHUNK,
    AUDIO,
    DEBOUNCE_TIME,
    THRESHOLD,
)
from utils.settings.assistant_settings import ASSISTANTS
from assistant.abstract_assistant import AbstractAssistant


class Astra:

    def __init__(self) -> None:
        self.model = Model(wakeword_models=["alexa"])
        self.wake_words: List[str] = ["alexa"]

        self.assistants: Dict[str, AbstractAssistant] = ASSISTANTS

        self.audio = pyaudio.PyAudio()
        self.mic_stream = AUDIO.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def listen(self) -> None:
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
                speech = self.listen_to_speech()
                assistant_id = self.determine_assistant(speech)
                assistant = self.assistants.get(assistant_id, None)
                if assistant:
                    assistant.respond(speech)
                print("Listening for wake words...")

    def listen_to_speech(self) -> Union[str, None]:
        speech = None
        with self.mic as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            speech = self.recognizer.recognize_google(audio, language="de-DE")
            print(speech)
        except sr.UnknownValueError:
            speech = None
            print("Could not understand audio")

        return speech

    def determine_assistant(self, speech: str) -> str:
        if not speech:
            return "Simple"
        
        # TODO: Let the classification be done by chatgpt
        if "Uhrzeit" in speech:
            return "Time"
        if "Witz" in speech:
            return "Joke"
        else:
            return "Simple"
