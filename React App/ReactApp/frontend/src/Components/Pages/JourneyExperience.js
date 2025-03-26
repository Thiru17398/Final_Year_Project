import React, { useState } from "react";
import { Link } from "react-router-dom";

import HomePage from "../Journey Experience Module/JourneysPage";
import { Outlet } from "react-router-dom";

import "./../../Styles/JourneyExperience.css"; // Import CSS styles

function JourneyExperience() {

  return (
    <div>
      <Outlet />
    </div>
  );
}

export default JourneyExperience;
