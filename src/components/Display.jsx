import React, { useRef } from 'react'
import * as tf from "@tensorflow/tfjs";
import * as posenet from "@tensorflow-models/posenet";
import Webcam from 'react-webcam';
import './../assets/styles/display.css'
import { drawKeypoints, drawSkeleton } from '../../util/utilities';

function Display() {
    const webcamRef = useRef(null);
    const canvasRef = useRef(null);
  
    //  Load posenet
    const runPosenet = async () => {
      const net = await posenet.load({
        inputResolution: { width: 500, height: 400 },
        scale: 0.5,
      });
      //
      setInterval(() => {
        detect(net);
      }, 100);
    };
  
    const detect = async (net) => {
      if (
        typeof webcamRef.current !== "undefined" &&
        webcamRef.current !== null &&
        webcamRef.current.video.readyState === 4
      ) {
        // Get Video Properties
        const video = webcamRef.current.video;
        const videoWidth = webcamRef.current.video.videoWidth;
        const videoHeight = webcamRef.current.video.videoHeight;
  
        // Set video width
        webcamRef.current.video.width = videoWidth;
        webcamRef.current.video.height = videoHeight;
  
        // Make Detections
        const pose = await net.estimateSinglePose(video);
        console.log(pose);
  
        drawCanvas(pose, video, videoWidth, videoHeight, canvasRef);
      }
    };
  
    const drawCanvas = (pose, video, videoWidth, videoHeight, canvas) => {
      const ctx = canvas.current.getContext("2d");
      canvas.current.width = videoWidth;
      canvas.current.height = videoHeight;
  
      drawKeypoints(pose["keypoints"], 0.6, ctx);
      drawSkeleton(pose["keypoints"], 0.7, ctx);
    };
  
    runPosenet();

  return (
    <div className='display'>
    <header className='display_header'>
      <Webcam 
        ref={webcamRef}
        style={{
          position: "absolute",
          marginLeft: "auto",
          marginRight: "auto",
          left: "0",
          right: "0",
          textAlign: "center",
          zindex: "9",
          width: "500px",
          height: "400px",
          "borderRadius": "16px"
        }}
      />
      <canvas 
        ref={canvasRef}
        style={{
          position: "absolute",
          marginLeft: "auto",
          marginRight: "auto",
          left: "0",
          right: "0",
          textAlign: "center",
          zindex: "9",
          width: "500px",
          height: "400px",
          "borderRadius": "8px"
        }}
      />

    </header>
  </div>
  )
}

export default Display