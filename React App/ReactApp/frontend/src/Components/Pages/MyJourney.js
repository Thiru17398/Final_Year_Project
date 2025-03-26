import React, { useEffect, useState , useRef} from "react";
import { FaMapMarkerAlt } from "react-icons/fa";
import { GoogleMap, LoadScript, DirectionsService, DirectionsRenderer } from "@react-google-maps/api";
import "./../../Styles/MyJourney.css";

const mapContainerStyle = {
  width: "100%",
  height: "400px",
};

const center = { lat: 13.0827, lng: 80.2707 }; // Default to Chennai

const MyJourney = () => {

  const apiKey = process.env.REACT_APP_API_KEY;
  const [source, setSource] = useState("");
  const [destination, setDestination] = useState("");
  const [directions, setDirections] = useState(null);

  const mapRef = useRef(null);

  const handleSearch = () => {
    const directionsService = new window.google.maps.DirectionsService();
    directionsService.route(
      {
        origin: source,
        destination: destination,
        travelMode: window.google.maps.TravelMode.TRANSIT, // Use public transport
      },
      (result, status) => {
        if (status === "OK") {
          setDirections(result);
        } else {
          alert("Error fetching directions: " + status);
        }
      }
    );
  };

  return (
    <div className="journey-container">
      <h2>Plan Your Journey</h2>

      <div className="search-options">
      <div className="input-group">
        <FaMapMarkerAlt className="icon" />
        <input
          type="text"
          value={source}
          className="input-field"
          placeholder="Enter Source"
          onChange={(e) => setSource(e.target.value)}
        />
      </div>

      <div className="input-group">
        <FaMapMarkerAlt className="icon" />
        <input
          type="text"
          value={destination}
          className="input-field"
          placeholder="Enter Destination"
          onChange={(e) => setDestination(e.target.value)}
        />
      </div>



      <button className="submit-btn" onClick={handleSearch}>
        Find Route
      </button>

      </div>
      <LoadScript googleMapsApiKey={apiKey}>
        <div className="map-container">
          <GoogleMap mapContainerStyle={mapContainerStyle} center={center} zoom={12}>
            {directions && <DirectionsRenderer directions={directions} />}
          </GoogleMap>
        </div>
      </LoadScript>
    </div>

    
  );
};

export default MyJourney;
