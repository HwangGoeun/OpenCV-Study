# selfie.py 코드 실행한 다음 오기

import cv2

def on_trackbar():
    pass

img_background = cv2.imread("./selfie/2.jpg", cv2.IMREAD_GRAYSCALE)
img_object = cv2.imread("./selfie/1.jpg", cv2.IMREAD_GRAYSCALE)

# 차영상 만들기
img_sub = cv2.subtract(img_object, img_background)

cv2.imshow('background', img_background)
cv2.imshow('object', img_object)
cv2.imshow('sub', img_sub)

cv2.namedWindow("Binary")
cv2.createTrackbar("threshold", "Binary", 0, 255, on_trackbar)
cv2.setTrackbarPos("threshold", "Binary", 127)

# 5-4.py 트랙바 코드 이용
while True:
    thresh = cv2.getTrackbarPos("threshold", "Binary")
    
    retval, img_binary = cv2.threshold(img_sub, thresh, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("Binary", img_binary)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()