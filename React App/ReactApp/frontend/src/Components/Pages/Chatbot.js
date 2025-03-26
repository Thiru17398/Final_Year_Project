import React from "react";
import { Link } from "react-router-dom";
import "./../../Styles/Chatbot.css"

function Chatbot() {
  return (
    <div className="container">
      <iframe

      src="http://localhost:8501"
      title="Embedded React App"
      width="100%"
      height="600px"
      style={{ border: "none" }}
      >

      </iframe>
    </div>
  );
}

export default Chatbot;
