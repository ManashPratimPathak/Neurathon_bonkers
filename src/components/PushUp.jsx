import React from "react";
import data from "./../data/yoga.json"
import "./../assets/styles/excercise.css"
import Display from './Display'
import FilePickerButton from "./filePickerButton";
import {Link} from "react-router-dom"


function PushUp(porps) {
  return (
    <div className="excercise_main">
      
      <div className="excercise_content">
        <div className="excercise_left_content">
        <div className='content_header'>
        <div className="excercise_Header">
        <h3>{data[0].name}</h3>
      </div>
          <h3>Steps</h3>
        </div>
          <ul>
            {data[0].steps.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
          <div className='content_header'>
          <h3>Precautions</h3>
        </div>
          <ul>
            {data[0].precautions.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
        </div>
        <div className="excercise_right_content">
          <FilePickerButton />
          <Link to="/result/pushUp">
            <button className='sample_button'>See sampled dataset</button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default PushUp;
