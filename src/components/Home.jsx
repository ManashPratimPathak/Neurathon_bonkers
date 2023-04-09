import React from 'react'
import './../assets/styles/hero.css'
import trainer_hero from "./../assets/images/trainer_hero.svg"

function Home() {
  return (
    <>
        <div className='Hero'>
            <div className='left_hero'>
                <div className='Left_hero_content_wrapper'>
                    <h1>NeuraFit</h1>
                    <p>Ready to improve your fitness and wellness? Click on the button now to get started! Our web app provides feedback and guidance on a variety of exercises, so you can be sure you're performing them correctly and safely. Whether you're a beginner or an experienced fitness enthusiast, our app is the perfect tool to help you achieve your goals.<br/><br/> Click the button below to start your journey to a stronger, healthier, and happier you. </p>
                    <div className='hero_button'>
                    <a href='/Menu'>
                        <button>Let's start</button>
                    </a>
                    </div>
                </div>
            </div>
            <div className='right_hero'>
                <div className='right_hero_content_wrapper'>
                    <img className="trainer_hero" alt="trainer_hero" src={trainer_hero}></img>
                </div>
            </div>
        </div>
        
    </>
  )
}

export default Home


//YoGAI.io "Ready to improve your yoga practice? Our web app provides real-time feedback and guidance on your yoga poses. Whether you're a beginner or an experienced yogi, our app is the perfect tool to help you achieve your goals