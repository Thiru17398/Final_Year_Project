import React from "react";
import { Link , Outlet } from "react-router-dom";
import  "./../../Styles/HomePage.css"// Import styles

function HomePage() {

  document.title = "Transit Simplified";

  return (
    <div>
      <nav className="navbar">
        <h2 className="logo">Transit Simplified</h2>
        <ul className="nav-links">
          <Link to="/">Home</Link>
          <Link to="/journey-experience">Journey Experience</Link>
          <Link to="/my-journey">My Journey</Link>
          <Link to="/chatbot">Chatbot</Link>
          <Link to="/live-updates">Live Updates</Link>
        </ul>
      </nav>
      <div className="content">
        <Outlet />
      </div>
    </div>
  );
}

export default HomePage;
