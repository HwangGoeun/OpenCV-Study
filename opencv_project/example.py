import cv2

img_color = cv2.imread("./opencv_project/test.jpg", cv2.IMREAD_COLOR)

if img_color is None:
    print("You can't read image")
    exit(1)

cv2.namedWindow('Color')
cv2.imshow('Color', img_color)

cv2.waitKey(0)
cv2.destroyAllWindows()