import numpy as np
import mediapipe as mp
from app import constants
import joblib

class GuestureRecognizer:
    def __init__(self):
        self.model = joblib.load("models/classifier.pkl")

    def recognizer(self,landmarks):
        if(len(landmarks)==0):
            return  "NO HAND"
        wrist_x = landmarks[0][1]
        wrist_y = landmarks[0][2]
        wrist_z = landmarks[0][3]

        row = []
        for lm in landmarks:
            _ ,x,y,z = lm
            row.extend([x-wrist_x,y-wrist_y,z-wrist_z])

        prediction = self.model.predict([row])

        # probabilty = self.model.predict_proba([row])

        # confidence = max(probabilty[0])
        # print(f"{prediction[0]} -> {confidence}")
        # if confidence < 0.30:
        #     return "Unknown"
        return prediction[0]
    

