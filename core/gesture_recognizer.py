import cv2
import numpy as np
import mediapipe as mp
from app import constants

class GuestureRecognizer:
    def recognizer(self,landmarks):
        if(len(landmarks)==0):
            return  "NO HAND"
        fingers =[]
        if(landmarks[4][1]>landmarks[3][1]):
            fingers.append(1)
        else:
            fingers.append(0)

        for tips in constants.TIP_IDS[1:]:
            if(landmarks[tips][2]<landmarks[tips-2][2]):
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)
        return constants.GESTURES.get(tuple(fingers),"UNKNOWN")
    

