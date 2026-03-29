import { Send, Mic, Plus } from "lucide-react";
import { useState, useRef } from "react";

function InputBar({ onSend }) {
  const [input, setInput] = useState("");
  const [listening, setListening] = useState(false);
  const [file, setFile] = useState(null);

  const fileInputRef = useRef(null);

  // 🎤 Voice recognition
  const handleVoice = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();
    setListening(true);

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
      setListening(false);
    };

    recognition.onerror = () => setListening(false);
  };

  // ➕ Ouvrir sélecteur fichiers
  const handleAttachClick = () => {
    fileInputRef.current.click();
  };

  // 📨 Envoyer texte + fichier
  const handleSend = () => {
    if (!input.trim() && !file) return;

    // On envoie un objet complet au parent
    onSend({ text: input, file });

    // Reset après envoi
    setInput("");
    setFile(null);
  };

  return (
    <div className="input-bar">
      <div className="input-wrapper">
        {/* + Bouton fichiers */}
        <button type="button" onClick={handleAttachClick} className="attach-btn">
          <Plus size={20} />
        </button>

        {/* Input caché fichiers */}
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: "none" }}
          onChange={(e) => setFile(e.target.files[0])}
          accept="image/*,.pdf,.txt"
        />

        {/* Input texte */}
        <input
          type="text"
          placeholder="Demander à JARVIS..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />

        {/* 🎤 Micro */}
        <button type="button" onClick={handleVoice} className="mic-btn">
          <Mic size={18} color={listening ? "red" : "black"} />
        </button>

        {/* 📨 Send */}
        <button type="button" onClick={handleSend} className="send-btn">
          <Send size={18} />
        </button>
      </div>

      {/* Preview fichier */}
      {file && (
        <div className="file-preview">
          📎 {file.name}
        </div>
      )}
    </div>
  );
}

export default InputBar;
