# 이미지 비트 연산

import cv2
import numpy as np

img_logo = cv2.imread('logo.png', cv2.IMREAD_COLOR)
img_back = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_logo, cv2.COLOR_RGB2GRAY)

# 로고 모양 틀 만들기
ret, img_mask = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

# 로고 모양 틀 반전 하기
img_mask_inv = cv2.bitwise_not(img_mask)

h, w = img_logo.shape[:2]
img_roi = img_back[0:h, 0:w]

# 로고 이미지에서 로고 모양틀 반전한 것 and 연산
img1 = cv2.bitwise_and(img_logo, img_logo, mask = img_mask_inv)
# 로고 이미지에서 로고 모양틀 만든 것 and 연산
img2 = cv2.bitwise_and(img_roi, img_roi, mask=img_mask)

dst = cv2.add(img1, img2)

img_back[0:h, 0:w] = dst

cv2.imshow('background', img_back)
cv2.waitKey(0)