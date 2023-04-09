import React from 'react'
import './../assets/styles/videoscreen.css'
function PullUpSample() {
    return (
        // diplay 2 video in a row from src folder 
        <div className='pushup_sample'>
            <div className='pushup_sample_video'>
                <p>User</p>
                <video width="640" height="480" controls>
                    <source src="/src/video/Pulluptrain.mp4" type="video/mp4" />
                </video>
            </div>
            <div className='pushup_sample_video'>
                <p>Professional Trainer</p>
                <video width="640" height="480" controls>
                    <source src="/src/video/Pulluptest.mp4" type="video/mp4" />
                </video>
            </div>
        </div>
    )
}

export default PullUpSample