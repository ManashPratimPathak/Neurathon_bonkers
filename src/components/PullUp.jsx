import React from 'react';
import data from "./../data/yoga.json"
import "./../assets/styles/excercise.css"
import Display from './Display'
import FilePickerButton from "./filePickerButton";


function PullUp() {
  return (
    <div className="excercise_main">
      <div className="excercise_content">
        <div className="excercise_left_content">
        <div className="excercise_Header">
        <h3>{data[2].name}</h3>
      </div>
        <div className='content_header'>
          <h3>Steps</h3>
        </div>
          <ul>
            {data[2].steps.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
          <div className='content_header'>
          <h3>Precautions</h3>
        </div>
          <ul>
            {data[1].precautions.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
        </div>
        <div className="excercise_right_content">
          <FilePickerButton />
        </div>
      </div>
    </div>
  )
}

export default PullUp