import cv2
import numpy as np

def detect_flower(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower=np.array([20,100,100])
    upper=np.array([35,255,255])

    mask=cv2.inRange(hsv,lower,upper)

    contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>500:
            x,y,w,h=cv2.boundingRect(cnt)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cx=x+w//2
            cy=y+h//2

            cv2.circle(frame,(cx,cy),5,(0,0,255),-1)

            cv2.putText(frame,"Tomato Flower",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,0),2)

            return frame,cx,cy,True

    return frame,0,0,False


if __name__=="__main__":
    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read()

        if not ret:
            break

        frame,x,y,found=detect_flower(frame)

        cv2.imshow("Flower Detection",frame)

        if cv2.waitKey(1)&0xFF==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
