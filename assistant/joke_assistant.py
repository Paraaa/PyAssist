import requests
import logging
from typing import Optional
from assistant.abstract_assistant import AbstractAssistant
from utils.settings.default_messages_settings import JOKE_RESPONSES

logger = logging.getLogger("JokeAssistant")


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
                    "text", JOKE_RESPONSES.get("JOKE_NOT_FOUND", "")
                )
                logger.debug(f"Fetched joke: {joke}")
            else:
                logger.error(
                    f"Failed to fetch joke with status code {response.status_code}"
                )
                return ""
            return joke
        except requests.RequestException as e:
            logger.exception(f"Error fetching joke: {str(e)}")
            return f"Fehler beim Abrufen des Witzes"

    def respond(self, speech: Optional[str] = "") -> None:
        joke = self.fetch_joke()
        self.say(joke)
