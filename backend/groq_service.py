from groq import Groq
import os

client = Groq(api_key=os.getenv("Gsk_MVDMnfJZpoagJYsT6TDDWGdyb3FY8p7Kz4n1ciDKbYVv98e4wwoS"))

def ask_ai(message, history):

    messages = []

    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["bot"]})

    messages.append({"role": "user", "content": message})

    chat = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages
    )

    return chat.choices[0].message.content
