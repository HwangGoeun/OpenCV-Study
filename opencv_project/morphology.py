import cv2
import numpy as np


img_gray = cv2.imread('morphology.png', cv2.IMREAD_GRAYSCALE)

kernel = cv2.getStructuringElement( cv2.MORPH_RECT, ( 3, 3 ) )

# erosion 침식
erosion = cv2.erode(img_gray.copy(), kernel, iterations = 3)

# dilation 확장
dilation = cv2.dilate(img_gray.copy(), kernel, iterations = 3)

# 이미지 두 개씩 합치기
result = cv2.hconcat([erosion, dilation])

cv2.imshow("original", img_gray)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()