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
# plt.plot(t1, arr, label = "line 1")
# plt.plot(t1, ans, label = "line 2")

bicepcurlsTrain=Aitrainer("AiTrainercurls.mp4")
arr=bicepcurlsTrain.accuracydetection()

bicepcurlsTest=Aitrainer("Bicepcurltest.mp4")
ans=bicepcurlsTest.accuracydetection()

arr,ans=bicepcurlsTest.upsample(arr,ans)

PushupTrain=Aitrainer("Pushuptrain.mp4")
parr=PushupTrain.accuracydetection()

Pushuptest=Aitrainer("Pushuptest.mp4")
pan=Pushuptest.accuracydetection()

parr,pan=Pushuptest.upsample(parr,pan)

from matplotlib import pyplot as plt
import seaborn as sns
data1 = cv2.VideoCapture('Pushuptrain.mp4')
frames = data1.get(cv2.CAP_PROP_FRAME_COUNT)
fps = data1.get(cv2.CAP_PROP_FPS)
l=len(arr)
# calculate duration of the video
seconds1 = int(frames / fps)+1
c1=seconds1/l
t1=[]
# v1=c1
for i in range(0,l):
    t1.append(round(c1*i,2))

    
    
PullupTrain=Aitrainer("Pulluptrain.mp4")
larr=PullupTrain.accuracydetection()


PullupTest=Aitrainer("Pulluptest.mp4")
lans=PullupTest.accuracydetection()


larr,lans=PullupTest.upsample(larr,lans)

data1 = cv2.VideoCapture('Pulluptrain.mp4')
frames = data1.get(cv2.CAP_PROP_FRAME_COUNT)
fps = data1.get(cv2.CAP_PROP_FPS)
l=len(arr)
# calculate duration of the video
seconds1 = int(frames / fps)+1
c1=seconds1/l
t1=[]
# v1=c1
for i in range(0,l):
    t1.append(round(c1*i,2))
print(t1)



# Analysis
from matplotlib import pyplot as plt
import numpy as np
import statistics

class datayl:
    def graph(self,array1,array2,time):
        x=time;
        y=array1;
        z=array2;
        plt.plot(x, y, color='r',label='array1')
        plt.plot(x, z, color='g',label='array2')
  
    def deviation(self,array1,array2):
        m=np.corrcoef(np.array((array1, array2)))[0, 1]
        return m
    def mean_accuracy(self,array1,array2):
        ans=[]
        l=len(array1)
        for i in range(l):
            ans.append(round(array2[i]/array1[i],2))
        m=statistics.mean(ans)
        m=m*100
        if m>100:
            m=m-100
            m=100-m
            
        return m
    BicepcurlTraindata = [259, 259, 259, 262, 266, 266, 270, 277, 282, 282, 286, 288, 290, 290, 291, 292, 293, 293, 293, 293, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 294, 293, 293, 293, 291, 291, 291, 290, 289, 287, 287, 285, 282, 278, 278, 275, 272, 270, 270, 269, 268, 267, 267, 266, 264, 263, 263, 260, 259, 256, 256, 255, 253, 250, 250, 246, 245, 242, 242, 239, 237, 234, 234, 230, 227, 223, 223, 217, 211, 208, 208, 203, 197, 195, 195, 192, 189, 188, 188, 186, 185, 185, 185, 184, 184, 185, 185, 184, 184, 185, 185, 185, 187, 187, 187, 188, 190, 192, 192, 194, 197, 201, 201, 204, 207, 211, 211, 214, 217, 220, 220, 223, 226, 228, 228, 229, 232, 236, 236, 241, 245, 249, 249, 254, 258, 263, 263, 267, 272, 277, 277, 280, 282, 285, 285, 287, 287, 288, 288, 288, 288, 288, 288, 289, 288, 289, 289, 289, 289, 289, 289, 288, 288, 288, 288, 289, 289, 289, 289, 290, 290, 289, 289, 289, 287, 287, 287, 286, 284, 282, 282, 280, 278, 276, 276, 273, 272, 270, 270, 269, 266, 264, 264, 262, 260, 257, 257, 253, 249, 247, 247, 244, 241, 239, 239, 234, 231, 227, 227, 223, 220, 217, 217, 214, 210, 207, 207, 204, 200, 197, 197, 194, 191, 188, 188, 188, 186, 186, 186, 185, 185, 185, 185, 184, 184, 184]
BicepcurlTestdata = [191, 191, 191, 192, 195, 197, 202, 205, 210, 214, 220, 227, 235, 243, 250, 254, 259, 265, 268, 271, 274, 277, 281, 284, 285, 286, 289, 293, 296, 299, 302, 303, 304, 306, 307, 308, 308, 309, 310, 311, 310, 310, 310, 310, 309, 309, 305, 302, 297, 293, 289, 285, 282, 280, 278, 274, 271, 266, 263, 261, 258, 252, 251, 250, 246, 244, 239, 237, 236, 233, 231, 225, 223, 221, 218, 216, 214, 211, 210, 207, 206, 205, 203, 202, 202, 201, 201, 201, 201, 200, 197, 195, 195, 195, 196, 200, 202, 207, 213, 219, 225, 233, 242, 248, 252, 257, 261, 266, 271, 275, 277, 281, 283, 284, 284, 286, 290, 293, 295, 297, 300, 300, 303, 305, 306, 307, 308, 308, 308, 309, 309, 309, 309, 308, 309, 307, 306, 303, 299, 295, 291, 288, 283, 281, 278, 275, 270, 265, 262, 260, 257, 251, 249, 247, 243, 242, 238, 233, 233, 231, 228, 225, 222, 220, 217, 215, 214, 210, 209, 205, 204, 201, 203, 202, 200, 199, 198, 198, 198, 198, 198, 198, 197, 195, 197, 197, 199, 200, 206, 210, 215, 221, 227, 234, 243, 246, 249, 253, 260, 262, 267, 269, 274, 277, 279, 282, 283, 285, 287, 290, 293, 296, 299, 301, 302, 304, 306, 307, 307, 308, 310, 310, 310, 310, 309, 309, 309, 309, 308, 306, 304, 301, 296, 292, 287, 283, 278, 276, 271, 269, 265]

PushupTraindata = [231, 230, 236, 238, 245, 255, 261, 269, 269, 277, 282, 285, 290, 290, 295, 296, 302, 305, 303, 305, 304, 302, 301, 301, 301, 301, 304, 302, 300, 298, 297, 289, 280, 278, 270, 267, 260, 250, 247, 238, 237, 228, 222, 219, 216, 214, 214, 215, 214, 216, 216, 218, 230, 237, 246, 246, 255, 266, 269, 275, 277, 286, 294, 296, 300, 303, 306, 304, 302, 303, 304, 305, 306, 306, 305, 306, 301, 293, 291, 283, 281, 274, 265, 259, 249, 247, 237, 230, 229, 226, 223, 219, 219, 218, 221, 222, 223, 230, 232, 239, 243, 251, 267, 269, 277, 280, 287, 296, 297, 303, 302, 302, 301, 301, 301, 301, 302, 304, 305, 303, 301, 292, 285, 284, 276, 271, 261, 250, 244, 234, 232, 226, 219, 214, 212, 211, 212, 213, 214, 216, 217, 226, 238, 242, 249, 251, 265, 276, 281, 288, 290, 297, 301, 301, 301, 301, 301, 301, 301, 301, 301, 304, 301, 296, 289, 287, 281, 271, 268, 258, 253, 242, 234, 232, 226, 224, 217, 214, 211, 210, 210, 212, 213, 214, 220, 222, 233, 253, 256, 262, 267, 274, 284, 286, 295, 297, 304, 305, 304, 304, 304, 302, 302, 302, 301, 301, 297, 287, 287, 279, 277, 269, 256, 253, 244, 242, 234, 228, 228, 223, 220, 218, 218, 217, 217, 217, 219, 226, 229, 240, 245, 254, 265, 267, 274, 280, 288, 297, 299, 302, 303, 303, 303, 301, 301, 301, 302, 303, 303, 300, 298, 293, 283, 280, 272, 271, 262, 251, 249, 236, 236, 229, 222, 220, 215, 211, 208, 208, 207, 208, 208, 210, 218, 221, 232, 236, 245, 260, 265, 274, 275, 282, 290, 295, 301, 302, 303, 303, 304, 304, 302, 302, 300, 300, 301, 301, 298, 291, 286, 280, 277, 270, 256, 251, 240, 238, 232, 225, 222, 216, 215, 211, 210, 210, 212, 212, 212, 222, 225, 236, 238, 248, 254, 256, 264, 266, 276, 289, 289, 298, 302, 306, 308, 307, 306, 305, 304, 304, 304, 302, 299, 299, 293, 290, 285, 283, 275, 272, 264, 254, 252, 244, 240, 231, 222, 219, 213, 210, 204, 204, 202, 204, 204, 207, 213, 216, 227, 231, 238, 245, 255, 266, 269, 276, 289, 289, 298, 301, 306, 307, 307, 308, 306, 304, 303, 303, 302, 302, 301, 293, 291, 283, 282, 275, 265, 262, 256, 252, 243, 233, 230, 222, 221, 216, 211, 206, 206, 205, 206, 208, 208, 213, 215, 228, 245, 247, 258, 260, 270, 280, 285, 291, 291, 298, 303, 305, 305, 302]
PushupTestdata =[199, 199, 199, 199, 185, 185, 201, 201, 208, 208, 208, 221, 221, 226, 226, 230, 230, 230, 233, 233, 236, 236, 239, 239, 239, 243, 243, 246, 246, 248, 248, 248, 253, 253, 256, 256, 258, 258, 258, 259, 259, 262, 262, 267, 267, 267, 268, 268, 272, 272, 274, 274, 274, 276, 276, 279, 279, 281, 281, 281, 284, 284, 286, 286, 289, 289, 289, 290, 290, 292, 292, 293, 293, 293, 295, 295, 296, 296, 299, 299, 299, 301, 301, 304, 304, 306, 306, 306, 307, 307, 306, 306, 305, 305, 305, 305, 305, 304, 304, 304, 304, 304, 304, 304, 304, 304, 305, 305, 305, 305, 305, 306, 306, 305, 305, 305, 303, 303, 301, 301, 298, 298, 298, 296, 296, 293, 293, 288, 288, 288, 287, 287, 283, 283, 281, 281, 281, 278, 278, 273, 273, 272, 272, 272, 270, 270, 276, 276, 268, 268, 268, 262, 262, 261, 261, 260, 260, 260, 257, 257, 254, 254, 252, 252, 252, 251, 251, 247, 247, 249, 249, 249, 249, 249, 248, 248, 246, 246, 246, 242, 242, 240, 240, 237, 237, 237, 235, 235, 232, 232, 228, 228, 228, 224, 224, 220, 220, 215, 215, 215, 212, 212, 208, 208, 203, 203, 203, 202, 202, 200, 200, 197, 197, 197, 191, 191, 184, 184, 182, 182, 182, 181, 181, 182, 182, 181, 181, 181, 181, 181, 180, 180, 181, 181, 181, 180, 180, 179, 179, 178, 178, 178, 178, 178, 179, 179, 183, 183, 183, 188, 188, 194, 194, 203, 203, 203, 207, 207, 202, 202, 213, 213, 213, 220, 220, 225, 225, 227, 227, 227, 231, 231, 235, 235, 239, 239, 239, 243, 243, 246, 246, 250, 250, 250, 253, 253, 255, 255, 258, 258, 258, 261, 261, 264, 264, 262, 262, 262, 265, 265, 267, 267, 271, 271, 271, 275, 275, 276, 276, 280, 280, 280, 285, 285, 285, 285, 286, 286, 286, 286, 286, 287, 287, 289, 289, 289, 294, 294, 296, 296, 297, 297, 297, 299, 299, 299, 299, 300, 300, 300, 300, 300, 301, 301, 304, 304, 304, 305, 305, 309, 309, 309, 309, 309, 310, 310, 310, 310, 310, 310, 310, 309, 309, 310, 310, 310, 310, 310, 310, 310, 308, 308, 309, 309, 309, 308, 308, 306, 306, 303, 303, 303, 299, 299, 295, 295, 293, 293, 293, 289, 289, 284, 284, 283, 283, 283, 280, 280, 273, 273, 268, 268, 268, 262, 262, 260, 260, 258, 258, 258, 255, 255, 251, 251, 250, 250, 250, 249, 249, 248, 248, 248, 248, 248, 248, 248, 245, 245]

PullupTraindata = [194, 194, 194, 194, 194, 195, 190, 191, 191, 192, 189, 183, 185, 186, 186, 185, 184, 182, 189, 188, 188, 182, 164, 140, 121, 115, 115, 97, 73, 59, 51, 47, 47, 43, 40, 39, 39, 39, 39, 40, 45, 57, 81, 85, 85, 107, 124, 140, 155, 156, 156, 164, 164, 166, 169, 166, 166, 166, 166, 164, 162, 161, 161, 163, 166, 166, 163, 164, 164, 163, 161, 159, 160, 161, 161, 157, 151, 141, 124, 119, 119, 100, 73, 53, 43, 47, 47, 41, 37, 34, 37, 37, 37, 38]
PullupTestdata = [44, 43, 39, 41, 42, 42, 48, 62, 75, 91, 109, 128, 135, 141, 151, 152, 160, 165, 164, 161, 157, 155, 155, 146, 138, 131, 120, 108, 92, 79, 66, 52, 45, 41, 41, 43, 44, 47, 53, 65, 82, 98, 111, 125, 135, 144, 150, 159, 164, 163, 160, 158, 157, 154, 146, 141, 132, 123, 111, 94, 80, 68, 56, 46, 40, 39, 36, 39, 43, 48, 57, 73, 91, 106, 119, 129, 145, 147, 150, 160, 165, 165, 162, 159, 158, 152, 148, 140, 133, 127, 122, 108, 94, 79]

fun= datayl()
b=fun.deviation(BicepcurlTraindata,BicepcurlTestdata)
c=fun.mean_accuracy(BicepcurlTraindata,BicepcurlTestdata)

print('mean deviation of bicepcurl:',b,'mean accuracy of bicepcurl:',c)

b=fun.deviation(PushupTraindata,PushupTestdata)
c=fun.mean_accuracy(PushupTraindata,PushupTestdata)

print('mean deviation of pushups:',b,'mean accuracy of pushups:',c)

b=fun.deviation(PullupTraindata,PullupTestdata)
c=fun.mean_accuracy(PullupTraindata,PullupTestdata)

print('mean deviation of pullups:',b,'mean accuracy of pullups:',c)



