import React from 'react'
import './../assets/styles/yogaCard.css'

function YogaCard(props) {
  return (
    <div className='yoga_card'>{props.name}</div>
  )
}

export default YogaCard