import cv2
from PIL import Image
from getRange import getRangeClr
cap= cv2.VideoCapture(0)
blue=[255, 0, 0]
while True:
    ret, frame=cap.read()

    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # if ret:
    #     cv2.imshow("frame", frame)
    
    lowerLimit, upperLimit=getRangeClr(color=blue)

    mask = cv2.inRange(hsvimage, lowerLimit, upperLimit)

    maskArray=Image.fromarray(mask)

    bbox=maskArray.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame=cv2.rectangle(frame, (x1, y1), (x2, y2), (0,0,255), 5)
    
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
