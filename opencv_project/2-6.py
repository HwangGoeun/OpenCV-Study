# video capture

import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("You can't open the camera")
    exit(1)

while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("Capture failure")
        break

    cv2.imshow("Color", img_frame)

    key = cv2.waitKey(0)

    if key == 27:
        break

print(type(ret))
print(type(img_frame))

cap.release()
cv2.destroyAllWindows()