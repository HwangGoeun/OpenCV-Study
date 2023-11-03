# gray scale

import cv2

img_color = cv2.imread("./opencv_project/test.jpg")

if img_color is None:
    print("You can't read the image")
    exit(1)

cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', img_gray)
cv2.imwrite('./opencv_project/grayscale.jpg', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()