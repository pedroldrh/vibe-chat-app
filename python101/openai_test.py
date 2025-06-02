import os
from openai import OpenAI

# 1. Grab API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

# 2. Instantiate the new client
client = OpenAI(api_key=api_key)

# 3. Send a simple chat request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, are you there?"}],
    max_tokens=20
)

# 4. Print out the reply
reply = response.choices[0].message.content
print("Model replied:", reply)

