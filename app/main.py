import cv2

from core.camera import Camera
from core.hand_tracker import HandTracker
from core.gesture_recognizer import GuestureRecognizer
from ui.overlay import Overlay
from services.dataset_collector import DatasetCollector
from core.gesture_smoother import GestureSmoother

camera = Camera()

smoothener = GestureSmoother()

tracker = HandTracker()

collector = DatasetCollector()


recognizer = GuestureRecognizer()

overlay = Overlay()

while True:

    frame = camera.getFrame()

    if frame is None:
        break

    frame, landmarks = tracker.detect_hands(frame)

    gesture = recognizer.recognizer(landmarks)
    gesture = smoothener.smooth(gesture)

    frame = overlay.draw_text(frame, gesture)

    cv2.imshow("Sign Language Translator", frame)

    key = cv2.waitKey(1) & 0xFF
    if ord('a')<=key<=ord('z'):
        label = chr(key).upper()
        collector.save_landmarks(landmarks,label)
        print(f"saved {label}")



    if key == ord('Q'):
        break

camera.release()

cv2.destroyAllWindows()