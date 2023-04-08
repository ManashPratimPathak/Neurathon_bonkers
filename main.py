import cv2
import mediapipe as mp
import numpy as np
import time
import math

class Aitrainer:
    def __init__(self,videoname):
        self.videoname=videoname
    def calangle(self,p1,p2,p3):
    
        self.x1,self.y1=int(p1[0]),int(p1[1])
        self.x2,self.y2=int(p2[0]),int(p2[1])
        self.x3,self.y3=int(p3[0]),int(p3[1])
        self.angle = math.degrees(math.atan2(self.y3 - self.y2, self.x3 - self.x2) -
                                 math.atan2(self.y1 - self.y2, self.x1 - self.x2))
        if self.angle < 0:
            self.angle += 360
        return int(self.angle)
    def upsample(self,a,b):
        
        l1=len(a)
        l2=len(b)
        if l1>l2:
            y=l1-l2
            # print(y,l2)
            x=round(l2/y)
            # print(x)
            ans=[]
            print(b)
            for i in range(0,l2,x):
                ans.append([b[i],i])
            # print(ans)
            for i in range(y):
                b.insert(ans[i][1]+i,ans[i][0])

        elif l1<l2:
            y=l2-l1
            # print(y,l2)
            x=round(l1/y)
            # print(x)
            ans=[]
            # print(b)
            for i in range(0,l1,x):
                ans.append([a[i],i])
            # print(ans)
            for i in range(y):
                a.insert(ans[i][1]+i,ans[i][0])


        return a,b
    
    def accuracydetection(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture(self.videoname)
        frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        seconds = round(frames / fps)+1
        start_time = time.time()
        arr=[]
        # Set the time limit (in seconds)
        time_limit = seconds
        with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
            

            while cap.isOpened():
                success, image = cap.read()
                h, w = image.shape[:2]
                if not success:
        #             print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
        #         mp_pose = mp.solutions.pose
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
                lm = results.pose_landmarks
                lmPose  = mp_pose.PoseLandmark

                if not results.pose_landmarks:
                    continue
                # print all landmarks position
        #         results.pose_landmarks

        #         x1=results.pose_landmark[11].x
        #         y1=results.pose_landmark[11].y
                x1 = int(lm.landmark[lmPose.LEFT_SHOULDER].x * w)
                y1 = int(lm.landmark[lmPose.LEFT_SHOULDER].y * h)
                x2=int(lm.landmark[lmPose.LEFT_ELBOW].x * w)
                y2=int(lm.landmark[lmPose.LEFT_ELBOW].y * h)
                x3=int(lm.landmark[lmPose.LEFT_WRIST].x * w)
                y3=int(lm.landmark[lmPose.LEFT_WRIST].y * h)
                p1=[x1,y1]
                p2=[x2,y2]
                p3=[x3,y3]
        #         arr=[]
                a=self.calangle(p1,p2,p3)
                arr.append(a)

                if time.time() - start_time > time_limit:
                    return arr

                    break
                # Draw the pose annotation on the image.
#                 image.flags.writeable = True
#                 image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#                 mp_drawing.draw_landmarks(
#                     image,
#                     results.pose_landmarks,
#                     mp_pose.POSE_CONNECTIONS,
#                     landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                # Flip the image horizontally for a selfie-view display.
        #         cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        cap.release()

bicepcurlsTrain=Aitrainer("AiTrainercurls.mp4")
arr=bicepcurlsTrain.accuracydetection()

bicepcurlsTest=Aitrainer("Bicepcurltest.mp4")
ans=bicepcurlsTest.accuracydetection()

arr,ans=bicepcurlsTest.upsample(arr,ans)
from matplotlib import pyplot as plt
import seaborn as sns
data1 = cv2.VideoCapture('AiTrainercurls.mp4')
frames = data1.get(cv2.CAP_PROP_FRAME_COUNT)
fps = data1.get(cv2.CAP_PROP_FPS)
l=len(arr)
# calculate duration of the video
seconds1 = int(frames / fps)+1
c1=seconds1/l
t1=[]
# v1=c1
for i in range(0,l):
    t1.append(c1*i)
plt.plot(t1, arr, label = "line 1")
plt.plot(t1, ans, label = "line 2")




