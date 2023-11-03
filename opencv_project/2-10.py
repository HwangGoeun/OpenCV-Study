import cv2

cap = cv2.VideoCapture("./opencv_project/output.avi")

if cap.isOpened() == False:
    print("You can't open the video")
    exit()

while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("Finish reading the video file")
        break

    cv2.imshow("Color", img_frame)

    key = cv2.waitKey(25)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()