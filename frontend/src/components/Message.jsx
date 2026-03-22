import ReactMarkdown from 'react-markdown';

function Message({ role, text }) {
  return (
    <div className={`message ${role}`}>
      {/* Si c'est l'IA, on utilise ReactMarkdown pour formater le texte */}
      {role === "ai" ? (
        <div className="markdown-content">
          <ReactMarkdown>{text}</ReactMarkdown>
        </div>
      ) : (
        /* Si c'est l'utilisateur, on laisse le texte simple */
        <span>{text}</span>
      )}
    </div>
  );
}

export default Message;
