import requests
from typing import Optional
from assistant.abstract_assistant import AbstractAssistant


class JokeAssistant(AbstractAssistant):

    def __init__(self):
        super().__init__()
        self.assistant_id = "Joke"

    def fetch_joke(self) -> str:
        url = "https://witzapi.de/api/joke"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                joke_data = response.json()
                joke = joke_data[0].get(
                    "text", "Entschuldigung, ich konnte keinen Witz abrufen."
                )
            return joke
        except requests.RequestException as e:
            return f"Fehler beim Abrufen des Witzes: {e}"

    def respond(self, speech: Optional[str] = "") -> None:
        joke = self.fetch_joke()
        self.say(joke)
