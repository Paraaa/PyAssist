from assistant.simple_assistant import SimpleAssistant
from assistant.time_assistant import TimeAssistant
from assistant.joke_assistant import JokeAssistant

ASSISTANTS = {
    "Simple": SimpleAssistant(),
    "Time": TimeAssistant(),
    "Joke": JokeAssistant(),
}
