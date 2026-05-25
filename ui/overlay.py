import cv2

class Overlay:
    def draw_text(self,frame,text):
        cv2.putText(frame,text,(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),3)
        return frame