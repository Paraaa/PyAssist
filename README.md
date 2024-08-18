# PyAssist
PyAssist is a virtual assistant similar to Alexa or Siri.


## What you need

- OpenAI api key
- create a `env.py` with the following variables:
```python
OPEN_AI_API_KEY="your_api_key"
```

## Notes
- Don't use the 2.1.6 version of the todoist api as it has the issue that project wont be correctly fetched
- The project id can be retrieved from the todoist page and is in the url: https://app.todoist.com/app/project/test-projekt-api-2337762329 -> 2337762329