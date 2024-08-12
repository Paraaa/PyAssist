from assistant.simple_chat_assistant import SimpleChatAssistant
from assistant.time_assistant import TimeAssistant
from assistant.joke_assistant import JokeAssistant
from assistant.unknown_assistant import UnknownAssistant
from assistant.timer_assistant import TimerAssistant
from assistant.todoist_assistant import TodoistAssistant

ASSISTANTS = {
    "Unknown": UnknownAssistant(),
    "SimpleChat": SimpleChatAssistant(),
    "Time": TimeAssistant(),
    "Joke": JokeAssistant(),
    "Timer": TimerAssistant(),
    "Todoist": TodoistAssistant(),
}
