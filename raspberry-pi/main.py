from camera import Camera
from flower_detection import detect_flower
from navigation import navigate,pollinate
import cv2

cam=Camera()

while True:
    frame=cam.get_frame()

    if frame is None:
        break

    frame,x,y,found=detect_flower(frame)

    if found:
        navigate(x)

        if abs(x-320)<30:
            pollinate()
    else:
        print("Searching for flower...")

    cv2.imshow("Smart Tomato Pollination Bot",frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
