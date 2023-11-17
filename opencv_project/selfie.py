import cv2
import sys

mode = 0    # 1 = Video, 2 = Photo
num = 1

cap = cv2.VideoCapture(0)
cap.set(3, 640)     # 너비 설정
cap.set(4, 320)     # 높이 설정
if cap.isOpened() == False:
    print("You can't open the camera")
    sys.exit(1)

while True:
    ret, frame = cap.read()     # 사진 촬영
    frame = cv2.flip(frame, 1)  # 좌우 대칭
    roi = frame[0: 300, :].copy()   # ROI. copy() 함수를 이용해 원본 이미지 수정 없이 실행하기

    cv2.imshow("Result", roi)

    if ret == False:
        print("Failed to capture")
        break

    if mode == 1:
        cv2.imwrite('./selfie/' + str(num) + '.jpg', roi) # 사진 저장
        num += 1    # 사진 몇 장 찍었는지~~
        mode = 0    # 비디오만 보여주는 모드로 변경
    
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('1'):   # 1번 누르면 사진 촬영됨
        mode = 1

cv2.destroyAllWindows()
