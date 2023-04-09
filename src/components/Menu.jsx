import React from 'react'
import Card from './Card';
import exerData from "./../data/yoga.json"
import './../assets/styles/menu.css'


function Menu() {
  return (
    <div className='Menu_page'>
      <div className='Menu_header'>
        <h1>Select an excercise</h1>
      </div>
      <div className='Menu_content'>
        {exerData.map((data) => {
          return <Card
            id={data.id}
            name={data.name}
            route={data.route}
            imgpath={data.imgpath} />
        })}
      </div>
    </div>
  )
}

export default Menu