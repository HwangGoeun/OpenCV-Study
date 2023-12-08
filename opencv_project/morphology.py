import cv2
import numpy as np


img_gray = cv2.imread('morphology.png', cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( 3, 3 ) )

# erosion 침식
erosion = cv2.erode(img_gray.copy(), kernel, iterations = 3)

# dilation 확장
dilation = cv2.dilate(img_gray.copy(), kernel, iterations = 3)

# opening
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
open = cv2.morphologyEx(img_gray.copy(), cv2.MORPH_OPEN, kernel)

# closing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
close = cv2.morphologyEx(img_gray.copy(), cv2.MORPH_CLOSE, kernel)

# 이미지 두 개씩 합치기
result1 = cv2.hconcat([erosion, dilation])
result2 = cv2.hconcat([open, close])
result = cv2.vconcat([result1, result2])

cv2.imshow("original", img_gray)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()