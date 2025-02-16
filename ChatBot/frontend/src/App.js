import React, { useState } from "react";

const App = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        if (!input) return;

        const newMessages = [...messages, { text: input, sender: "user" }];
        setMessages(newMessages);

        

        const request = new Request("http://localhost:5000/api/chatbot/message" , {
            method : 'POST',
            headers : {
                'Content-Type' : 'application/json'
                },
            body : JSON.stringify({ message : input }) 
        })

        const response = await fetch(request);
        const data = await response.json();
        
        setMessages([...newMessages , {text : data.response , sender : "bot"}]);
        
        setInput("");
    };

    return (
        <div style={{ maxWidth: "400px", margin: "auto", padding: "20px", textAlign: "center" }}>
            <h2>Chatbot</h2>
            <div style={{ border: "1px solid black", height: "300px", overflowY: "scroll", padding: "10px" }}>
                {messages.map((msg, index) => (
                    <div key={index} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
                        <strong>{msg.sender}:</strong> {msg.text}
                    </div>
                ))}
            </div>
            <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Ask me about transit..." />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default App;
