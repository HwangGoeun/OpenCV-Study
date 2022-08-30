# velog : https://velog.io/@hwang_gim/%EC%A1%B0%EB%8F%84-%EA%B0%92-%EB%B0%94%EA%BF%94%EC%84%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0

import cv2
from imutils import paths   # 이미지 경로 탐색을 위한 라이브러리

cnt = 0

for imagePath in paths.list_images("D:\\OpenCV\\illuminance change\\"):
    original_img = cv2.imread(imagePath)
    changed_img = cv2.add(original_img, (50, 50, 50, 50))         # 이미지 밝기 밝게
    changed_img2 = cv2.add(original_img, (-50, -50, -50, -50))    # 이미지 밝기 어둡게
    
    cv2.imwrite("D:\\OpenCV\\illuminance change\\" + str(cnt) + ".png", changed_img)
    cnt += 1
    cv2.imwrite("D:\\OpenCV\\illuminance change\\" + str(cnt) + ".png", changed_img2)
    cnt += 1

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()