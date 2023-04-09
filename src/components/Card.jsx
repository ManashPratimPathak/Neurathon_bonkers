import React from 'react'
import './../assets/styles/yogaCard.css'
import { Link } from "react-router-dom"

function YogaCard(props) {
  return (
    <Link to={`/${props.route}`}> <img key={props.id} src={props.imgpath} className='yoga_card' /></Link>
  )
}

export default YogaCard