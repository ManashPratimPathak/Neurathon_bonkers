import React from 'react'
import './../assets/styles/yogaCard.css'
import {Link} from "react-router-dom"

function YogaCard(props) {
  return (
   <Link to={`/${props.route}`}> <div key={props.id} className='yoga_card'>{props.name}</div></Link>
  )
}

export default YogaCard