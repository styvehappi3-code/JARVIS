import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyC_Wd8mlbog0D_FzofiJNsaH-mqMxsLvHE"))
model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
Tu es un assistant ton nom c'est javis repont a toute les question pas trop long
"""
def ask_gemini(message, history):

    conversation = SYSTEM_PROMPT + "\n"

    for h in history:
        conversation += f"Patient: {h['user']}\nAssistant: {h['bot']}\n"

    conversation += f"Patient: {message}\nAssistant:"

    try:
        response = model.generate_content(conversation)
        return response.text.strip()
    except Exception as e:
        print("ERREUR GEMINI:", e)
        return "Reformule la question medical"

