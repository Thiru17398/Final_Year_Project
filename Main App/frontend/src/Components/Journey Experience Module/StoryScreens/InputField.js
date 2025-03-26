import React from 'react'
import '../../Css/AddStory.css'

const InputField = (props) => {
  return (
    <div className='input-field'>
        <label htmlFor="source" className = "fields"> {props.field} : </label>

    <input
    className='fields'
    type={props.type}
    required
    id={props.id}
    placeholder={props.placeholder}
    onChange={(e) => props.setValue(e)}
    value={props.value}   
    />
    </div>
  )
}

export default InputField