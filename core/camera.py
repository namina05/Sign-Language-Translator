import cv2
from app.config import *

class Camera :
    def __init__(self):
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(3,FRAME_WIDTH)
        self.cap.set(4,FRAME_HEIGHT)

    def getFrame(self):
        success,frame = self.cap.read()

        if(not success):
            return None
        
        frame = cv2.flip(frame,1)
        
        return frame
    
