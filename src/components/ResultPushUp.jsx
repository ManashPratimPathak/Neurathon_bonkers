import React from 'react'
import Chart2 from './../components/Chart2'
import staticData from "./../data/static.json"

function ResultPushUp() {
  return (
    <div className='result_section'><Chart2/>
      <p> {staticData[1].meanDeviation}</p>
      <p> {staticData[1].accuracy}</p>
    </div>
  )
}

export default ResultPushUp