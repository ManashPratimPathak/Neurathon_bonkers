import React from 'react'
import YogaCard from './YogaCard';
import './../assets/styles/menu.css'

const yoga = ["tree","chair", "cobra"];

function Menu() {
  return (
    <div className='Menu_page'>
      <div className='Menu_header'>
        <h3>Select an Yoga</h3>
      </div>
      <div className='Menu_content'>
        {yoga.map((item)=>{
          return <YogaCard name={item}/>
        })}
      </div>
    </div>
  )
}

export default Menu