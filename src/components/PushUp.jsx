import React from "react";
import data from "./../data/yoga.json"
import "./../assets/styles/excercise.css"
import Display from './Display'

function PushUp(porps) {
  return (
    <div className="excercise_main">
      <div className="excercise_Header">
        <h3>{data[0].name}</h3>
      </div>
      <div className="excercise_content">
        <div className="excercise_left_content">
          <ul>
            {data[0].steps.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
        </div>
        <div className="excercise_right_content"><Display /></div>
      </div>
    </div>
  );
}

export default PushUp;
