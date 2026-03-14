import axios from "axios";

const API = axios.create({
  baseURL: "https://jarvis-api-08dr.onrender.com",
});

export const sendMessage = async (sessionID, message) => {
  const response = await API.post("/chat", {
    session_id: sessionID,
    message: message,
    ctx:{}
  });
  return response.data;
};

