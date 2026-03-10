import google.generativeai as genai
import os

def ask_gemini(message, history):
    # 1. On vérifie si la clé est bien lue
    api_key = os.getenv("API_KEY") # Vérifie que c'est bien le nom sur Render
    
    if not api_key:
        print("ERREUR CRITIQUE : La variable API_KEY est vide !")
        return "Erreur : Clé API manquante dans l'environnement."

    print(f"DEBUG : Tentative avec la clé commençant par : {api_key[:5]}...")

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Test simple sans historique d'abord pour isoler le problème
        response = model.generate_content(message)
        return response.text.strip()

    except Exception as e:
        # On affiche l'erreur complète pour la voir dans les logs Render
        print(f"ERREUR DÉTAILLÉE : {type(e).__name__}: {e}")
        return f"Erreur technique : {type(e).__name__}"
