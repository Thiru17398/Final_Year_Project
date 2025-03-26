import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./../../Styles/LiveUpdates.css"; // Import CSS styles

function LiveUpdates() {
  const [updates, setUpdates] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");

  // Simulating real-time updates with mock data
  useEffect(() => {
    const mockUpdates = [
      { id: 1, vehicle: "Train #A23", message: "Delayed by 10 minutes", time: "2 mins ago" },
      { id: 2, vehicle: "Bus 22", message: "Rerouted due to roadwork", time: "5 mins ago" },
      { id: 3, vehicle: "Taxi", message: "Heavy traffic near downtown", time: "10 mins ago" },
    ];

    // Simulating real-time updates every 5 seconds
    const interval = setInterval(() => {
      const newUpdate = {
        id: updates.length + 1,
        vehicle: `Bus ${Math.floor(Math.random() * 10)}`, // Random vehicle
        message: `New transport update #${updates.length + 1}`,
        time: "Just now",
      };
      setUpdates((prevUpdates) => [newUpdate, ...prevUpdates]);
    }, 5000);

    setUpdates(mockUpdates); // Initial updates

    return () => clearInterval(interval); // Cleanup interval
  }, []);

  // Handle search input
  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  // Filter updates based on search query
  const filteredUpdates = updates.filter((update) =>
    update.vehicle.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="page-container">
      <h1 className="page-title">Live Updates</h1>
      <p className="page-description">
        Stay informed with real-time transport updates.
      </p>

      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search vehicle (e.g., Bus 22, Train A23)"
        value={searchQuery}
        onChange={handleSearchChange}
        className="search-bar"
      />

      {/* Display Live Updates */}
      <div className="update-list">
        {filteredUpdates.length === 0 ? (
          <p>No matching updates found.</p>
        ) : (
          filteredUpdates.map((update) => (
            <div key={update.id} className="update-card">
              <h3>{update.vehicle}</h3>
              <p>{update.message}</p>
              <small>{update.time}</small>
            </div>
          ))
        )}
      </div>

      <Link to="/" className="back-button">Back to Home</Link>
    </div>
  );
}

export default LiveUpdates;
