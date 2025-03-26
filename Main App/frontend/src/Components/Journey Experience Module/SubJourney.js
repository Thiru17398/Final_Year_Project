import React from 'react'
import InputField from './InputField'

const SubJourney = (props) => {

  console.log(props.value)
  


  return (
    <div className='sub-journey'>
        <h4>Journey #{props.no}</h4>
        <InputField field = "Starting Point" type = "text" id = "startingPoint" placeholder = "Ex : Guindy"  setValue = {props.setValue} value = {props.value['startingPoint']}/>
        <InputField field = "Ending Point" type = "text" id = "endingPoint" placeholder = "Ex : R M K Engineering College" setValue = {props.setValue} value = {props.value['endingPoint']} />
        <InputField field = "Journey Duration" type = "text" id = "duration" placeholder = "Duration of this Journey (Ex : 50 min)" setValue = {props.setValue} value = {props.value['duration']} />
        <InputField field = "Cost" type = "text" id = "cost" placeholder = "Cost of this Journey (Ex : 25 Rs)" setValue = {props.setValue} value = {props.value['cost']} />
        <InputField field = "Transportation Used" type = "text" id = "transportation" placeholder = "Ex : Bus/Train with (Bus No/Train Name)" setValue = {props.setValue} value = {props.value['transportation']} />
        <InputField field = "Transport Frequency" type = "text" id = "frequency" placeholder = "Frequence of a Bus/Train (Ex : Every 10 min)" setValue = {props.setValue} value = {props.value['frequency']} />
        <InputField field = "Overall Experience and Suggestion" type = "text" id = "experience" placeholder = "Ex : Take Last Coach for Quicker Exit" setValue = {props.setValue} value = {props.value['experience']} />
    </div>
  )
}

export default SubJourney;