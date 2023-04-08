import React from 'react'
import data from "./../data/yoga.json"
import "./../assets/styles/excercise.css"
import Display from './Display'

function BicepCurl() {
  return (
    <div className="excercise_main">
      
      <div className="excercise_content">
        <div className="excercise_left_content scroll">
        <div className='content_header'>
        <div className="excercise_Header">
        <h3>{data[1].name}</h3>
      </div>
          <h3>Steps</h3>
        </div>
          <ul>
            {data[1].steps.map((item)=>{
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
        <div className="excercise_right_content"></div>
      </div>
    </div>
  )
}

export default BicepCurl