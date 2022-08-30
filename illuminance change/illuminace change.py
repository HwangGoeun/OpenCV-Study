# velog : https://velog.io/@hwang_gim/%EC%A1%B0%EB%8F%84-%EA%B0%92-%EB%B0%94%EA%BF%94%EC%84%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0

import cv2
from imutils import paths   # 이미지 경로 탐색을 위한 라이브러리
import time                 # 1초 딜레이 주는 데에 쓴 라이브러리

for imagePath in paths.list_images("D:\\OpenCV\\illuminance change"):
    original_img = cv2.imread(imagePath)
    resize_img = cv2.resize(original_img, (300, 300))           # 이미지 크기 변경
    changed_img = cv2.add(resize_img, (50, 50, 50, 50))         # 이미지 밝기 밝게
    changed_img2 = cv2.add(resize_img, (-50, -50, -50, -50))    # 이미지 밝기 어둡게
    
    # 이미지 보여주기
    cv2.imshow('original', resize_img)
    cv2.imshow('changed', changed_img)
    cv2.imshow('changed2', changed_img2)
    time.sleep(1)

    key = cv2.waitKey(1)

    if key == 27:
        break

cv2.destroyAllWindows()