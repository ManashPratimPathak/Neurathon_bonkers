import React from 'react'
import Chart from './../components/Chart'
import "./../assets/styles/result.css"
import staticData from "./../data/static.json"

function ResultBicepCurl() {
  return (
    <div className='result_section'>
      <Chart/>
      <p> {staticData[0].meanDeviation}</p>
      <p> {staticData[0].accuracy}</p>
    </div>
  )
}

export default ResultBicepCurl