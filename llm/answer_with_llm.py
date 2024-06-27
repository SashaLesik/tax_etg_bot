from litellm import completion
import os

## set ENV variables
messages = [{ "content": "Hello, how are you?","role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)
print(response)