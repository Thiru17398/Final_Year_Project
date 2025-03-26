import React, { useRef, useContext, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { AuthContext } from "../../Context/AuthContext";
import { AiOutlineUpload } from 'react-icons/ai';
import { FiArrowLeft } from 'react-icons/fi';
import '../../Css/AddStory.css';
import InputField from './InputField';
import SubJourney from './SubJourney';

const AddStory = () => {
    const { config } = useContext(AuthContext);
    const imageEl = useRef(null);
    const editorEl = useRef(null);
    
    const [image, setImage] = useState(null);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [success, setSuccess] = useState('');
    const [error, setError] = useState('');
    
    const [journeyDetails, setJourneyDetails] = useState({
        source: "",
        destination: "",
        totalDuration:"",
        journeys: [{
            startingPoint: "",
            endingPoint: "",
            duration: "",
            cost: "",
            transportation:"",
            frequency: "",
            experience: ""
        }]
    });

    const handleChange = (e) => {
        setJourneyDetails(prevState => ({
            ...prevState,
            [e.target.id]: e.target.value
        }));
    };

    const handleSubJourneyChange = (index, e) => {
        setJourneyDetails(prevState => {
            // Ensure journeys array exists before modifying it
            const updatedJourneys = prevState.journeys ? [...prevState.journeys] : [];
    
            // Ensure index exists in journeys array
            if (!updatedJourneys[index]) {
                updatedJourneys[index] = {
                    startingPoint: "",
                    endingPoint: "",
                    duration: "",
                    cost: "",
                    transportation:"",
                    frequency: "",
                    experience: ""
                };
            }
    
            // Update the specific journey's field
            updatedJourneys[index] = {
                ...updatedJourneys[index],
                [e.target.id]: e.target.value
            };
    
            return { ...prevState, journeys: updatedJourneys };
        });
    };

    const addJourney = () => {
        setJourneyDetails(prevState => ({
            ...prevState,
            journeys: [...prevState.journeys, {
                startingPoint: "",
                endingPoint: "",
                duration: "",
                cost: "",
                transportation:"",
                frequency: "",
                experience: ""
            }]
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            await axios.post("/story/addJourneyExperience", journeyDetails, config);
            setSuccess('Journey added successfully!');
            setJourneyDetails({ source: "", destination: "", totalDuration:"", journeys: [{ startingPoint: "", endingPoint: "", duration: "", cost: "", frequency: "", experience: "" }] });
            
            setTimeout(() => setSuccess(''), 7000);
        } catch (error) {
            setError(error.response?.data?.error || 'Something went wrong');
            setTimeout(() => setError(''), 7000);
        }
    };

    return (
        <div className="Inclusive-addStory-page">
            <Link to={'/'}><FiArrowLeft /></Link>
            <form onSubmit={handleSubmit} className="addStory-form">
                <h1>My Journey Experience</h1>
                {error && <div className="error_msg">{error}</div>}
                {success && <div className="success_msg">{success} <Link to="/">Go home</Link></div>}

                <div className='input-fields'>
                    <InputField field="Source" type="text" id="source" placeholder="Source" setValue={handleChange} value={journeyDetails.source} />
                    <InputField field="Destination" type="text" id="destination" placeholder="Destination" setValue={handleChange} value={journeyDetails.destination} />
                    <InputField field="Total Journey Duration" type = "text" id = "totalDuration" placeholder = "Total Duration of the Journey" setValue = {handleChange} value = {journeyDetails.totalDuration} />
                    <h2>Journey Details</h2>
                    <div className='sub-journeys'>
                        {journeyDetails && journeyDetails.journeys.map((journey, index) => (
                            <SubJourney key={index} no={index + 1} setValue={(e) => handleSubJourneyChange(index, e)} value={journey} />
                        ))}
                    </div>
                    <button type="button" onClick={addJourney} className='addJourney-btn'>Add Journey</button>
                </div>

                <button type='submit' className='addStory-btn'>Post</button>
            </form>
        </div>
    );
};

export default AddStory;
