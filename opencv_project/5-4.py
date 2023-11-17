# 트랙바를 이용해 binary image 만들기

import cv2
import sys

def on_trackbar():
    pass

img_color = cv2.imread("document.jpg", cv2.IMREAD_COLOR)
if img_color is None:
    print("Error 1")
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale", img_gray)

cv2.namedWindow("Binary")
cv2.createTrackbar("threshold", "Binary", 0, 255, on_trackbar)
cv2.setTrackbarPos("threshold", "Binary", 127)

while True:
    thresh = cv2.getTrackbarPos("threshold", "Binary")

    # retval, img_binary = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY_INV)
    retval, img_binary = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)

    cv2.imshow("Binary", img_binary)

    if cv2.waitKey(1) & 0xFF == 27:
        break