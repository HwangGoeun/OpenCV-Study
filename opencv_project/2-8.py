# save the video

import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print("You can't open the camera")
    exit(1)

ret, img_frame = cap.read()

if ret == False:
    print("Capture failure")
    exit(1)

codec = cv2.VideoWriter.fourcc('M', 'J', 'P', 'G')

fps = 30.0

h, w = img_frame.shape[:2]

writer = cv2.VideoWriter("./opencv_project/output.avi", codec, fps, (w, h))

if writer.isOpened() == False:
    print("Can't ready for video file")
    exit(1)

while(True):
    ret, img_frame = cap.read()

    if ret == False:
        print("Capture failure")
        break

    cv2.imshow("Video", img_frame)

    writer.write(img_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
writer.release()

cv2.destroyAllWindows()