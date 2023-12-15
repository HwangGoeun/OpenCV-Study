import cv2

open_img_gray = cv2.imread('opening.png', cv2.IMREAD_GRAYSCALE)
close_img_gray = cv2.imread('closing.png', cv2.IMREAD_GRAYSCALE)

# opening
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
open = cv2.morphologyEx(open_img_gray.copy(), cv2.MORPH_OPEN, kernel)

# closing
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
close = cv2.morphologyEx(close_img_gray.copy(), cv2.MORPH_CLOSE, kernel)

result1 = cv2.hconcat([open_img_gray, open])
result2 = cv2.hconcat([close_img_gray, close])

cv2.imshow("opening", result1)
cv2.imshow("closing", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()
