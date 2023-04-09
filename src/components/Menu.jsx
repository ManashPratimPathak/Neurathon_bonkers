import React from 'react'
import Card from './Card';
import exerData from "./../data/yoga.json"
import './../assets/styles/menu.css'


function Menu() {
  return (
    <div className='Menu_page'>
      <div className='Menu_header'>
        <h3>Select an excercise</h3>
      </div>
      <div className='Menu_content'>
        {exerData.map((data)=>{
          return <Card 
          id={data.id} 
          name={data.name} 
          route={data.route}/>
        })}
      </div>
    </div>
  )
}

export default Menu