import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(message, history):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return str(e)
