# 결과 같이 보기

import cv2
import sys

img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("You can't read the image")
    sys.exit(1)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_canny = cv2.Canny(img_gray, 90, 180)

img_result1 = cv2.hconcat([img_gray, img_canny])
# 수직 방향으로 연결하고 싶다면
# img_result = cv2.vconcat([img_gray, img_canny])

cv2.imshow("Result", img_result1)
cv2.waitKey(0)

cv2.destroyAllWindows()