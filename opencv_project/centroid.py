import cv2 as cv
from random import randint

img_color = cv.imread('picture.png', cv.IMREAD_COLOR)

# 그레이 스케일 변환 후 바이너리로 변환
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 10, 255, cv.THRESH_BINARY_INV)
cv.imshow("img", img_binary)

# 이진화 결과를 개선하기 위한 모폴로지 연산
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
img_binary = cv.morphologyEx(img_binary, cv.MORPH_CLOSE, kernel)

# 컨투어 검출
# contours = 윤곽선을 나타내는 점의 리스트
# hierarchy = 윤곽선 간의 관계를 설명하는 배열
# RETR_LIST = 윤곽선 간의 관계 설명 X, 단순히 모든 윤곽선을 리스트로 반환
# CHAIN_APPROX_SIMPLE = 윤곽선을 구성하는 점들 중 일부만 저장해 메모리 줄이기
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, 
                        cv.CHAIN_APPROX_SIMPLE)

# 컨투어 그리기
# 인덱스 값을 -1으로 하면 모든 컨투어를 그릴 수도 있음.
for i in enumerate(contours):
    cv.drawContours(img_color, contours, i, (randint(0, 255), randint(0, 255), randint(0, 255)), cv.FILLED)  
# cv.drawContours(img_color, contours, 1, (0, 255, 0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)

# 컨투어 영역 크기 구하기
for i, contour in enumerate(contours):
    area = cv.contourArea(contour)

    print(i, '-', area)

cv.imshow("result", img_color)
cv.waitKey(0)
'''
# 컨투어 무게 중심 구하기
for contour in contours:
    # moments() = 이미지의 형태와 관련된 여러 속성들을 반환함.
    mu = cv.moments(contour)
    # m00: 영역 면적
    # m10: x축에 대한 모멘트
    # m01: y축에 대한 모멘트
    # m20, m11, m02: x와 y에 대한 모멘트의 제곱 및 곱에 대한 값들로, 이를 통해 중심축에 대한 정보를 얻을 수 있습니다.
    # m30, m21, m12, m03: x와 y에 대한 모멘트의 세제곱 및 곱에 대한 값들
    # mu20, mu11, mu02: 중심을 기준으로 한 x와 y에 대한 중심 모멘트
    # mu30, mu21, mu12, mu03: 중심을 기준으로 한 x와 y에 대한 중심 모멘트의 세제곱 및 곱에 대한 값들
    # nu20, nu11, nu02: 중심을 기준으로 한 x와 y에 대한 정규화된 중심 모멘트
    # 1e-5 = 0.00001, 아주 작은 값을 더해서 분모가 0이 되는 것 방지
    cx = int(mu['m10']/mu['m00'] + 1e-5)
    cy = int(mu['m01']/mu['m00'] + 1e-5)
    cv.circle(img_color, (cx, cy), 15, (0,255,255), -1)
'''
cv.imshow("result", img_color)
cv.waitKey(0)