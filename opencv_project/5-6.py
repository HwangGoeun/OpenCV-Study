# 적응형 이진화

import cv2
import sys

img_color = cv2.imread("document.jpg", cv2.IMREAD_COLOR)
if img_color is None:
    print("Error 1")
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# 마지막 C = 평균에서 뺄 상수. 값이 증가하면 그만큼 더 어두워지고(밝은 사진에서 사용), 값이 감소하면 그만큼 더 밝아진다(어두운 사진에서 사용).
img_binary = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 4)

cv2.imshow("GrayScale", img_gray)
cv2.imshow("Binary", img_binary)
cv2.waitKey(0)