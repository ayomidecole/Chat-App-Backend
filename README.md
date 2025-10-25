Building an AI powered backend with FASTAPI and the OpenAI API.

1. Created a virtual environment to keep the dependencies isolated.

You can recreate the virtual environment by running the following command:
```bash
python -m venv fastapi-openai
source fastapi-openai/bin/activate
pip install -r requirements.txt
```

2. Created a routes folder to keep the routes organized. We then create a file called `__init__.py`. This file is used to tell Python that the routes folder is a package.

3. Create the route. We created a post route

## Learnings

1. I used the python logging module for the first time. I used logger.debug() to debug by seeing what data the api receives, lets me track if the API is working properly and trobleshooting

2. I bundled up the chat functionality into a file openai_helper.py. This file contains the chat_helper function which is used to send messages to the OpenAI API.

```python
import logging
from typing import List, Dict
from fastapi import HTTPException
from config import client

logger = logging.getLogger(__name__)

async def chat_helper(message: Dict, model: str = 'gpt-5',
                      system_configuration: str = 'You are a helpful assistant',
                      message_history: List[Dict] = []):
    messages = [{'role': 'system', 'content': system_configuration}] + message_history + [message]
    logger.debug(f'chat_helper - Sending messages: {messages}')
    try:
        completion = client.responses.create(
            model=model,
            messages=messages
        )

        logger.debug({f'chat_helper - Received completion: {completion}'})
        response_message = {
            'role': 'assistant',
            'content': completion.choicrs[0].message,
            'refusal': None
        }
        return response_message
    except Exception as e:
        logger.error(f'chat_helper - Error: {e}')
        raise HTTPException(status_code=500, detail=str(e))
```

The `chat_helper` function is a convenient way to interact with an AI assistant. Below is how it works, explained using snippets from the actual code:

```python
async def chat_helper(message: Dict, model: str = 'gpt-5',
                      system_configuration: str = 'You are a helpful assistant',
                      message_history: List[Dict] = []):
```
This function takes in the user's message, an optional `model`, a `system_configuration` (which sets the assistant's personality), and a `message_history` (to track your previous conversation).

```python
messages = [{'role': 'system', 'content': system_configuration}] + message_history + [message]
```
Here, it builds the list of messages to send—starting with a "system" message (to set the assistant's behavior), followed by the conversation history and the user's new message.

```python
completion = client.responses.create(
    model=model,
    messages=messages
)
```
This line sends your conversation to the OpenAI API using the provided model and receives a response from the assistant.

```python
response_message = {
    'role': 'assistant',
    'content': completion.choicrs[0].message,
    'refusal': None
}
return response_message
```
After receiving the AI's response, it formats everything neatly into a dictionary, making it easy to use in your app.

If there’s an error—like a problem with the API or your internet connection—this code catches it and raises an HTTP error with details:

```python
except Exception as e:
    logger.error(f'chat_helper - Error: {e}')
    raise HTTPException(status_code=500, detail=str(e))
```

In short, `chat_helper` takes care of formatting messages, sending them to OpenAI, and handling any errors, so you don't have to manage the low-level details yourself.

3. We created a `config.py` file to store the OpenAI API key.

```python
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

This `config.py` file is responsible for securely setting up the connection to the OpenAI API:

- First, it imports the necessary packages: `openai` for interacting with the API, `os` for environment variable access, and `load_dotenv` for loading variables from a `.env` file.
- It then loads the environment variables from a `.env` file, which usually contains sensitive information like your OpenAI API key.
- The last part creates an `OpenAI` client using your secret API key (retrieved securely from the environment), which means you don't have to hard-code the key into your code. This client is then imported and used throughout your application to make requests to OpenAI.

**In short:**  
This file lets you keep your API key private and easily manage your OpenAI connection, so other parts of your code can just use the `client` object without worrying about authentication or configuration.
