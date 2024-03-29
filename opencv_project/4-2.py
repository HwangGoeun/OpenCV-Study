# track bar

import cv2

def on_trackbar(x):
    pass

cv2.namedWindow("Canny")

cv2.createTrackbar("low threshold", "Canny", 0, 1000, on_trackbar)
cv2.createTrackbar("high threshold", "Canny", 0, 1000, on_trackbar)

cv2.setTrackbarPos("low threshold", "Canny", 50)
cv2.setTrackbarPos("high threshold", "Canny", 150)

img_color = cv2.imread("test.jpg", cv2.IMREAD_COLOR)
img_gray = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Color", img_color)

while(1):
    low = cv2.getTrackbarPos("low threshold", "Canny")
    high = cv2.getTrackbarPos("high threshold", "Canny")

    img_canny = cv2.Canny(img_gray, low, high)

    cv2.imshow("Canny", img_canny)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()