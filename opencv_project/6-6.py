import cv2
import numpy as np

img_logo = cv2.imread('logo.png', cv2.IMREAD_COLOR)
img_back = cv2.imread('test.jpg', cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img_logo, cv2.COLOR_RGB2GRAY)
ret, img_mask = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

img_mask_inv = cv2.bitwise_not(img_mask)

h, w = img_logo.shape[:2]
img_roi = img_back[0:h, 0:w]

img1 = cv2.bitwise_and