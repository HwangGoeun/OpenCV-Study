import cv2
import numpy as np

img = cv2.imread('noise.png')

kernel = np.ones((5,5), np.float32)/25

# blur
blur = cv2.filter2D(img.copy(), -1, kernel)

# averaging blurring
avg_blur = cv2.blur(img.copy(), (5, 5))

# gaussian blurring
gaussian_blur = cv2.GaussianBlur(img.copy(), (5, 5), 0)

# median blurring
median_blur = cv2.medianBlur(img.copy(), 5)

# bilateral filtering
bilateral_blur = cv2.bilateralFilter(img.copy(), 5, 75, 75)

# 이미지 두 개씩 합치기
result1 = cv2.hconcat([blur, avg_blur])
result2 = cv2.hconcat([median_blur, bilateral_blur])
result = cv2.vconcat([result1, result2])

cv2.imshow("original", img)
cv2.imshow("result", result)
cv2.waitKey(0)