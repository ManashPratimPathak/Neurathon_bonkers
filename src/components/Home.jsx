import React from 'react'
import './../assets/styles/hero.css'
import yoga_gif from "./../assets/images/yoga_hero.gif"

function Home() {
  return (
    <>
        <div className='Hero'>
            <div className='left_hero'>
                <div className='Left_hero_content_wrapper'>
                    <h1>Project_neurathon</h1>
                    <p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, </p>
                    <div className='hero_button'>
                    <a href='/Menu'>
                        <button>Let's start</button>
                    </a>
                    </div>
                </div>
            </div>
            <div className='right_hero'>
                <div className='right_hero_content_wrapper'>
                    <img className="yoga_pic" alt="yoga_pic" src={yoga_gif}></img>
                </div>
            </div>
        </div>
        
    </>
  )
}

export default Home


//YoGAI.io "Ready to improve your yoga practice? Our web app provides real-time feedback and guidance on your yoga poses. Whether you're a beginner or an experienced yogi, our app is the perfect tool to help you achieve your goals