import React from 'react'
import Chart3 from './../components/Chart3'
import staticData from "./../data/static.json"

function ResultPullUp() {
  return (
    <div className='result_section'><Chart3/>
      <div className='result_other_details'>
        <p>Mean Deviation: {staticData[2].meanDeviation}</p>
        <p>Accuracy: {staticData[2].accuracy}</p>
      </div>
    </div>
  )
}

export default ResultPullUp