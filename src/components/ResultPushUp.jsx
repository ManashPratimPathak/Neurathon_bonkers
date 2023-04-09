import React from 'react'
import Chart2 from './../components/Chart2'
import staticData from "./../data/static.json"

function ResultPushUp() {
  return (
    <div className='result_section'><Chart2/>
      <div className='result_other_details'>
        <p>Mean Deviation: {staticData[1].meanDeviation}</p>
        <p>Accuracy: {staticData[1].accuracy}</p>
      </div>
    </div>
  )
}

export default ResultPushUp