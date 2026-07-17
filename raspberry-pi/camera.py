import cv2
from config import *

class Camera:
    def __init__(self):
        self.cap=cv2.VideoCapture(CAMERA_ID)
        self.cap.set(3,FRAME_WIDTH)
        self.cap.set(4,FRAME_HEIGHT)

    def get_frame(self):
        ret,frame=self.cap.read()
        if ret:
            return frame
        return None

    def release(self):
        self.cap.release()

if __name__=="__main__":
    cam=Camera()
    while True:
        frame=cam.get_frame()
        if frame is None:
            break
        cv2.imshow("Smart Tomato Pollination Bot",frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
