import React from 'react'
import Chart from './../components/Chart'
import "./../assets/styles/result.css"
import staticData from "./../data/static.json"

function ResultBicepCurl() {
  return (
    <div className='result_section'>
      <Chart/>
      <div className='result_other_details'>
        <p>Mean Deviation {staticData[0].meanDeviation}</p>
        <p>Accuracy {staticData[0].accuracy}</p>
      </div>
    </div>
  )
}

export default ResultBicepCurl