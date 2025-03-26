import React, { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom';
import SkeletonStory from './Skeletons/SkeletonStory';
import axios from "axios";
import { v4 as uuidv4 } from 'uuid';
import MyLocationIcon from '@mui/icons-material/MyLocation';
import CardStory from "./CardStory";
import NoStories from "./StoryScreens/NoStories";
import Pagination from './GeneralScreens/Pagination';
import SwapHorizIcon from '@mui/icons-material/SwapHoriz';
import './../../Styles/Home.css'
import { FaMapMarkerAlt } from "react-icons/fa";
import SearchIcon from '@mui/icons-material/Search';
import CreateIcon from '@mui/icons-material/Create';
import { Link } from 'react-router-dom';

const JourneysPage = () => {
  const suggestions = [
    "Chennai Central",
    "Koyambedu",
    "Guindy",
    "Tambaram",
    "T Nagar",
    "Anna Nagar",
    "Velachery",
    "Adyar",
    "Egmore",
    "Perambur",
  ];

    const [journeys , setJourneys] = useState([]);
    const [loading , setLoading] = useState(true);

    const [page, setPage] = useState(1);
    const [pages, setPages] = useState(1);

    const [source, setSource] = useState("");
    const [destination, setDestination] = useState("");

    const [filteredSource, setFilteredSource] = useState([]);
    const [filteredDestination, setFilteredDestination] = useState([]);
    const [showSourceDropdown, setShowSourceDropdown] = useState(false);
    const [showDestinationDropdown, setShowDestinationDropdown] = useState(false);
  
    const handleSubmit = (e) => {
      e.preventDefault();
    };

    const handleSourceSelect = (place) => {
      setSource(place);
      setShowSourceDropdown(false);
    };
  
    const handleDestinationSelect = (place) => {
      setDestination(place);
      setShowDestinationDropdown(false);
    };

    const handleSourceChange = (e) => {
      const value = e.target.value;
      setSource(value);
      if (value.length > 0) {
        setFilteredSource(suggestions.filter((s) => s.toLowerCase().includes(value.toLowerCase())));
        setShowSourceDropdown(true);
      } else {
        setShowSourceDropdown(false);
      }
    };
  
    const handleDestinationChange = (e) => {
      const value = e.target.value;
      setDestination(value);
      if (value.length > 0) {
        setFilteredDestination(suggestions.filter((d) => d.toLowerCase().includes(value.toLowerCase())));
        setShowDestinationDropdown(true);
      } else {
        setShowDestinationDropdown(false);
      }
    };

    const swapSourceAndDestination = () => {
      setSource(destination);
      setDestination(source)
      setShowSourceDropdown(false);
      setShowDestinationDropdown(false);
    }

    

    const navigate = useNavigate();


    useEffect(() => {
        const getJourneys = async () => {

            setLoading(true);

            try {

                const { data } = await axios.get(`http://localhost:5000/getAllJourneys`);
                
        
                if (source || destination) {
                  navigate(`/journey-experience?from=${source || ""}&to=${destination || ""}&page=${page}`);
                }
                else {
                  navigate({
                    pathname: '/journey-experience',
                    search: `${page > 1 ? `page=${page}` : ""}`,
                  });
        
        
                }
                setJourneys(data || []);
                setPages(1);
        
                setLoading(false);
              }
              catch (error) {
                setLoading(true)
                setJourneys([]);
              }
        }

        getJourneys();
    },[source , destination]);



  return (
    <div className="Inclusive-home-page">

      <div className='post'>
            <Link className="submit-btn" to={"/journey-experience/addJourney"}>
            <CreateIcon />
                Post My Journey Experience
            </Link>
      </div>

<div className="container">



      <div className="input-group">
        <FaMapMarkerAlt className="icon" />
        <input
          type="text"
          value={source}
          className="input-field"
          placeholder="Enter Source"
          onChange={handleSourceChange}
        />
        {showSourceDropdown && (
          <div className="suggestions">
            {filteredSource.map((loc, index) => {
              return(
                <div className='suggestion' onClick={() => handleSourceSelect(loc)}>
                <MyLocationIcon />
              <span key={index} >
                {loc}
              </span>
              </div>
              );
            }
            )
          }
          </div>
        )}
      </div>

      <SwapHorizIcon sx={{margin:"auto 0px",cursor:"pointer"}} onClick = {swapSourceAndDestination}/>

      {/* Destination Input */}
      <div className="input-group">
        <FaMapMarkerAlt className="icon" />
        <input
          type="text"
          value={destination}
          className="input-field"
          placeholder="Enter Destination"
          onChange={handleDestinationChange}
        />
        {showDestinationDropdown && (
          <div className="suggestions" >
            {filteredDestination.map((loc, index) => {
              return(
                <div className='suggestion' onClick={() => handleDestinationSelect(loc)}>
                <MyLocationIcon />
              <span key={index} >
                {loc}
              </span>
              </div>
              );
            }
            )}
          </div>
        )}
      </div>
      <button className="submit-btn">
        <SearchIcon />        
        Search Journeys
      </button>
    </div>

         {loading ?

            <div className="skeleton_emp">
            {
                [...Array(6)].map(() => {
                return (
                    // theme dark :> default : light
                    <SkeletonStory key={uuidv4()} />
                )
                })}
            </div>

            :
            <div>
            <div className="story-card-wrapper">
                {(journeys ?? []).length > 0 ?
                journeys.map((journey) => {
                    return (
                    <CardStory key={uuidv4()} journey={journey} />
                    )
                }) : <NoStories />
                }

            </div>

            <Pagination page={page} noOfPages={pages} changePage={setPage} />

            </div>

            }
            <br />
    </div>
  )
}

export default JourneysPage;