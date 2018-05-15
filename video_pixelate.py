import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
flags = [
cv2.COLOR_RGB2BGR,
 cv2.COLOR_RGB2BGRA,
 cv2.COLOR_RGB2GRAY,
 cv2.COLOR_RGB2HLS,
 cv2.COLOR_RGB2HLS_FULL,
 cv2.COLOR_RGB2HSV,
 cv2.COLOR_RGB2HSV_FULL,
 cv2.COLOR_RGB2LAB,
 cv2.COLOR_RGB2LUV,
 cv2.COLOR_RGB2RGBA,
 cv2.COLOR_RGB2XYZ,
 cv2.COLOR_RGB2YCR_CB,
 cv2.COLOR_RGB2YUV,
 cv2.COLOR_RGB2YUV_I420,
 cv2.COLOR_RGB2YUV_IYUV,
 cv2.COLOR_RGB2YUV_YV12]


def switch_flag():
    
    for num, flag in enumerate(flags):
        while(True):    
            ret, frame = cap.read()
            frame = cv2.cvtColor(frame, flag)
            for i in range(frame.shape[0]):
                if i % 20 == 0:
                    for j in range(frame.shape[1]):
                        if j % 20 == 0:
                            x = frame[i:i+49,j:j+49].mean(axis=0).mean(axis=0)
                            frame[i:i+49,j:j+49] = x

            
            cv2.imshow('frame{}'.format(num),frame)
         
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    

switch_flag()


cap.release()
cv2.destroyAllWindows()

