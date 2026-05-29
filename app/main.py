import cv2
import app.sharedframe as shared_frame
from core.camera import Camera
from core.hand_tracker import HandTracker
from core.gesture_recognizer import GuestureRecognizer
from services.dataset_collector import DatasetCollector
from core.gesture_smoother import GestureSmoother
from app.predictions import latest_prediction

def start_recognition():
    camera = Camera()

    smoothener = GestureSmoother()

    tracker = HandTracker()

    collector = DatasetCollector()


    recognizer = GuestureRecognizer()


    while True:

        frame = camera.getFrame()

        if frame is None:
            latest_prediction["camera_available"] = False
            continue

        latest_prediction["camera_available"] = True

        frame, landmarks = tracker.detect_hands(frame)
        _, buffer = cv2.imencode(".jpg", frame)
        shared_frame.latest_frame = buffer.tobytes()

        gesture,confidence = recognizer.recognizer(landmarks)
        gesture = smoothener.smooth(gesture)
        latest_prediction["predictions"] = gesture
        latest_prediction["confidence"] = confidence
        if(gesture=="NO HAND"):
            latest_prediction["hand_detected"] = False
        else:
            latest_prediction["hand_detected"] = True

        # frame = overlay.draw_text(frame, gesture)

        # cv2.imshow("Sign Language Translator", frame)

        # key = cv2.waitKey(1) & 0xFF
        # if ord('a')<=key<=ord('z'):
        #     label = chr(key).upper()
        #     collector.save_landmarks(landmarks,label)
        #     print(f"saved {label}")



        # if key == ord('Q'):
        #     break

    camera.release()

    cv2.destroyAllWindows()