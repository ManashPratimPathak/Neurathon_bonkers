import React from 'react'
import Chart3 from './../components/Chart3'
import staticData from "./../data/static.json"

function ResultPullUp() {
  return (
    <div className='result_section'><Chart3/>
      <p> {staticData[2].meanDeviation}</p>
      <p> {staticData[2].accuracy}</p>
    </div>
  )
}

export default ResultPullUp