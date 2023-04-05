import React from 'react'
import YogaCard from './YogaCard';
import './../assets/styles/main.css'

const yoga = ["tree","chair", "cobra"];

function Main() {
  return (
    <div className='Main_page'>
      <div className='Main_header'>
        <h3>Select an Yoga</h3>
      </div>
      <div className='Main_content'>
        {yoga.map((item)=>{
          return <YogaCard name={item}/>
        })}
      </div>
    </div>
  )
}

export default Main