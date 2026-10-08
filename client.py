import os
from dotenv import load_dotenv
from openai import OpenAI

# pip install openai
# if you saved the key under a different environment variable name, you can do something like:
load_dotenv()

command = "hey"
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)