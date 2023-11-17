import cv2
import sys

img_color = cv2.imread("gradation_color.png", cv2.IMREAD_COLOR)
if img_color is None:
    print("Error 1")
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

retval, img_binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Grayscale", img_gray)
cv2.imshow("Binary", img_binary)
cv2.waitKey(0)