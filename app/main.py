import cv2

from core.camera import Camera
from core.hand_tracker import HandTracker
from core.gesture_recognizer import GuestureRecognizer
from ui.overlay import Overlay

camera = Camera()

tracker = HandTracker()

recognizer = GuestureRecognizer()

overlay = Overlay()

while True:

    frame = camera.getFrame()

    if frame is None:
        break

    frame, landmarks = tracker.detect_hands(frame)

    gesture = recognizer.recognizer(landmarks)

    frame = overlay.draw_text(frame, gesture)

    cv2.imshow("Sign Language Translator", frame)

    if cv2.waitKey(1) == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()