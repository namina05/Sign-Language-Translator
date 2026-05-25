import cv2
import mediapipe as mp

from app import config


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            min_detection_confidence=config.DETECTION_CONFIDENCE,
            min_tracking_confidence=config.TRACKING_CONFIDENCE
        )

        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        hand_landmarks = []

        results = self.hands.process(rgb)

        if results.multi_hand_landmarks:

            hdlms = results.multi_hand_landmarks[0]

            self.mp_draw.draw_landmarks(
                    frame,
                    hdlms,
                    self.mp_hands.HAND_CONNECTIONS
                )

            h, w, c = frame.shape

            for id, lm in enumerate(hdlms.landmark):

                hand_landmarks.append((id, lm.x, lm.y,lm.z))

        return frame, hand_landmarks