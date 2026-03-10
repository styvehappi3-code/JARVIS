import google.generativeai as genai
import os

# 1. Récupération PROPRE de la clé
# Sur Render, tu dois créer une variable nommée "API_KEY" dans l'onglet Environment
api_key = os.getenv("API_KEY") 

if not api_key:
    print("ERREUR : La variable d'environnement API_KEY est vide !")
else:
    genai.configure(api_key=api_key)

# 2. Configuration du modèle (Une seule fois)
# On utilise le paramètre 'system_instruction' pour que JARVIS garde sa personnalité
SYSTEM_PROMPT = """
Tu es JARVIS, un assistant intelligent et polyvalent.
Réponds de manière claire, concise et naturelle.
Aide l’utilisateur pour toutes sortes de questions, de façon amicale et compréhensible.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def ask_gemini(message, history):
    """Envoie le message au modèle et gère l'historique."""
    
    # On utilise le système de chat natif de Gemini, c'est plus robuste
    chat_history = []
    for h in history:
        chat_history.append({"role": "user", "parts": [h['user']]})
        chat_history.append({"role": "model", "parts": [h['bot']]})

    try:
        chat = model.start_chat(history=chat_history)
        response = chat.send_message(message)
        return response.text.strip()
    except Exception as e:
        # On affiche l'erreur dans les logs Render pour savoir POURQUOI ça rate
        print(f"ERREUR GEMINI DÉTAILLÉE : {e}")
        return "Monsieur, un problème technique empêche ma réponse. Vérifiez mes logs."
