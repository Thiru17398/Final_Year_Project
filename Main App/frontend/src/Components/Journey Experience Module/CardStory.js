import React , {useState} from 'react';
import { Link } from 'react-router-dom';

const Journey = ({ journey }) => {

    // const editDate = (createdAt) => {
    //     const monthNames = ["January", "February", "March", "April", "May", "June",
    //     "July", "August", "September", "October", "November", "December"
    //     ];
    //     const d = new Date(createdAt);
    //     var datestring = d.getDate() + " " +monthNames[d.getMonth()] + " ," + d.getFullYear() 
    //     return datestring
    // }

    const [title , setTitle] = useState(journey.source + " - " + journey.destination);

    const subJourneys = journey.journeys;
    var totalCost = 0;

    subJourneys.forEach((j) => {
        totalCost += parseInt(j.cost);
    });

    totalCost = Number(totalCost) || 0;



    const truncateTitle= (title) => {
        const trimmedString = title.substr(0, 69);
        return trimmedString
    }


    return (

        <div className="story-card">
            <Link to={`/journey/${journey.id}`} className="story-link">

                <img className="story-image" src={`data:image/jpeg;base64,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`}  />
                <div className="story-content-wrapper">

                    <h5 className="story-title">
                        
                    {
                        title.length > 76 ? truncateTitle(title)+"..." : title
                    
                    }
                    </h5>

                    <div className='journey-info'>
                        <p className='duration'> Duration : <span>{journey.totalDuration}</span></p>
                        <p className='cost'>Cost : <span>{totalCost}</span></p>
                    </div>


                     
                </div>
            </Link>
        </div>

    )
}

export default Journey;
