# velog : https://velog.io/@hwang_gim/%ED%94%84%EB%A0%88%EC%9E%84-%EC%88%98-%EA%B3%84%EC%82%B0%ED%95%B4%EC%84%9C-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0

import cv2      # opencv 실행에 필요한 라이브러리 호출
import time     # fps 계산 시 사용

# 카메라 연결
# 프로그램 종료 시 출력되는 경고 메시지 방지를 위한 두 번쨰 아규먼트 지정
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 카메라 연결 실패 시 메시지 출력 후 프로그램 종료
if cap.isOpened() == False:
    print("Camera is not opened")
    exit(1)

prevTime = time.time()

# 카메라에서 얻은 이미지를 계속해서 출력하기 위한 반복문 실행
while True:
    # 카메라에서 얻은 이미지 읽어오기
    ret, img = cap.read()

    # 이미지를 받아오지 못 할 경우 메시지 출력 후 반복문 탈출
    if ret == False:
        print("Capture failed")
        break

    # 이미지 좌우 반전
    img = cv2.flip(img, 1)

    # 프레임 수 계산
    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    prevTime = curTime
    # 프레임 수 문자열에 저장
    fps_str = "FPS : %0.1f" %fps

    # 문자열 표시
    cv2.putText(img, fps_str, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
    # 얻은 이미지 Camera 윈도우를 통해 출력
    cv2.imshow('Camera', img)

    # 1초 동안 키보드 입력을 기다리기
    key = cv2.waitKey(1)

    # ESC 키를 눌렀을 때 반복문 탈출
    if key == 27:
        break

cap.release()               # 카메라와 연결을 종료
cv2.destroyAllWindows()     # 모든 창 닫기