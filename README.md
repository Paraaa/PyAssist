# PyAssist
PyAssist is a open-source virtual voice assistant built using Python. It uses the OpenAI's ChatGPT API to handle natural language requests in german.

## Table of Contents

- [Capabilities](#capabilities)
- [Installation and Setting Up](#installation-and-setting-up)
- [Writing Your Own Assistant](#writing-your-own-assistant)
- [Configuration Options](#configuration-options)


## Capabilities

PyAssist currently supports the following functionalities:

- Todo management through integration with Todoist
- Timer functionality
- Joke telling
- Simple chat conversations
- Get the current time


## Installation and Setting Up

To install and set up PyAssist, follow these steps:

1. Clone the repository: 
    ```bash
    git clone https://github.com/yourusername/PyAssist.git
    cd PyAssist
    ```
2. Create a virtual environment via `pyvenv` or `conda`: 
    ```bash
    # pyvenv
    python -m venv venv` 
    source venv/bin/activate

    # conda
    conda create -n pyassist python=3.11
    conda activate pyassist
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the necessary environment variables:
    - Create a file named `env.py` in the root directory
    - Add the following variables:
        ```python
        OPEN_AI_API_KEY="your_openai_api_key"
        TODOIST_API_KEY ="your_todoist_api_key"
        ```

5. Configure the Todoist project ID:
    - Open `utils/settings/todoist_settings.py`
    - Set the `PROJECT_ID` variable to your desired project in which PyAssist will create tasks
    The project ID can be retrieved from your todoist project url: https://app.todoist.com/app/project/test-projekt-api-[PROJECT_ID].

6. Run PyAssist by executing:
    ```bash
    python main.py
    ```

## Writing Your Own Assistant

PyAssist is designed to be extensible, allowing you to create custom assistants. To write your own assistant, you'll need to implement a few key components and derive from specific classes. 
For a full implementation look the assistants and LLMs in the directories `assistant/` and `LLM/`.

### 1. Derive from AbstractAssistant

Your custom assistant should derive from the `AbstractAssistant` class. This class provides basic functionality for speech recognition, text-to-speech conversion, and logging.

```python
from assistant.abstract_assistant import AbstractAssistant
from LLM.my_custom_llm import MyCustomLLM

class MyCustomAssistant(AbstractAssistant): 
    def init(self): 
        super().init() 
        # Initialize the name of the Assistant.
        # Note: This name has to match with the one you use in `utils/settings/assistant_settings.py`!
        self.assistant_id = "MyCustomAssistant" 

        # Define your custom llm class which you have to implement
        self.my_custom_llm = MyCustomLLM()

    def respond(self, speech: Optional[str] = "") -> None:
        # Implement your custom logic here
        pass
```

### 2. Implement the respond Method

The `respond` method is the core of your assistant. It should process the user's speech and determine the appropriate action.

```python
def respond(self, speech: Optional[str] = "") -> None: 
    if not speech: 
        return
    # Process the speech and determine the action. The speech is the raw text spoken by the user.
    action = self.my_custom_llm.process(speech=speech)

    if action == "custom_action":
        self.perform_custom_action()
    elif action == "another_action":
        self.perform_another_action()
    else:
        self.say(DEFAULT_RESPONSES.get("ERROR", ""))
```


### 3. Create a Language Model (LLM) for Your Assistant

You'll need to create a custom LLM to process user input and generate responses. This should derive from the `LLM` class.

```python
 from LLM.abstract_llm import LLM

class MyCustomLLM(LLM): def init(self): super().init()

    def process(self, *args, **kwargs):
        speech = kwargs.get("speech", "")
        if not speech:
            return
        
        prompt = self.format_prompt(speech)
        response = self.ask(prompt)
        # If you specify that the LLM should return a JSON response you should to the self.to_json() function. 
        # Otherwise return the plain text.
        return self.to_json(response)
        
    def format_prompt(self, prompt: str = ""):
        # Implement your custom prompt formatting logic here
        return prompt
```

### 4. Register Your Assistant

To make your assistant available to PyAssist, you need to register it in the `ASSISTANTS` dictionary in `utils/settings/assistant_settings.py`.
```python
from assistant.simple_chat_assistant import SimpleChatAssistant
# ...
from assistant.my_custom_assistant import MyCustomAssistant # Import your custom assistant

ASSISTANTS = { 
    "Unknown": UnknownAssistant(), 
    # ...
    "MyCustom": MyCustomAssistant(), # Add your custom assistant here 
}

```

## Configuration Options

PyAssist offers several configuration options to customize its behavior:

### Audio Settings

Modify `utils/settings/audio_settings.py` to adjust microphone input parameters and wake word detection thresholds. These settings allow you to fine-tune the assistant's responsiveness to voice commands and improve overall audio quality.

### Language Model Settings

Configure the language model and history length in `utils/settings/llm_settings.py`. This allows you to:

- Choose between different pre-trained language models from OpenAI


### Assistant Settings

Customize available assistants in `utils/settings/assistant_settings.py`. This allows you to:

- Enable or disable specific assistants (e.g., Todoist, timer, joke teller)
- Add custom assistants or modify existing ones

### Additional Configuration

- **Logging**: Modify `utils/logging_config.py` to adjust log levels and output formats.
- **Default response messages**: Update `utils/settings/default_messages_settings.py` to change the format and content of assistant responses.