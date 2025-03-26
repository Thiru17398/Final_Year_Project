import React from "react";
import { Routes, Route } from "react-router-dom";
import HomePage from "./Components/Pages/HomePage";
import MyJourney from "./Components/Pages/MyJourney";
// import {Chatbot}  from "chatbot";

import Chabot from "./Components/Pages/Chatbot"
import JourneyExperience from "./Components/Pages/JourneyExperience";
import LiveUpdates from "./Components/Pages/LiveUpdates";
import WelcomePage from "./Components/Pages/WelcomePage";
import JourneysPage from "./Components/Journey Experience Module/JourneysPage";
import AddJourney from "./Components/Journey Experience Module/AddJourney";
import TransportDashboard from "./Components/Pages/TransportDashboard";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />}>
        <Route index element = {<WelcomePage />} />
        <Route path="/my-journey" element={<MyJourney />} />
        <Route path="/journey-experience" element={<JourneyExperience />}>
            <Route index element = {<JourneysPage />} />
            <Route path="addJourney" element = {<AddJourney />} />
        </Route>
        <Route path="/chatbot" element={<Chabot />} />
        <Route path="/live-updates" element={<TransportDashboard />} />
      </Route>
    </Routes>
  );
}

export default App;