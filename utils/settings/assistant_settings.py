from assistant.simple_assistant import SimpleChatAssistant
from assistant.time_assistant import TimeAssistant
from assistant.joke_assistant import JokeAssistant
from assistant.unknown_assistant import UnknownAssistant

ASSISTANTS = {
    "Unknown": UnknownAssistant(),
    "SimpleChat": SimpleChatAssistant(),
    "Time": TimeAssistant(),
    "Joke": JokeAssistant(),
}
