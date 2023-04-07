import React from 'react'
import data from "./../data/yoga.json"
import "./../assets/styles/excercise.css"

function BicepCurl() {
  return (
    <div className="excercise_main">
      <div className="excercise_Header">
        <h3>{data[1].name}</h3>
      </div>
      <div className="excercise_content">
        <div className="excercise_left_content">
          <ul>
            {data[1].steps.map((item)=>{
                return( <li>{item}</li>)
            })}
          </ul>
        </div>
        <div className="excercise_right_content">{/* <Display /> */}</div>
      </div>
    </div>
  )
}

export default BicepCurl