# velog : https://velog.io/@hwang_gim/%EC%B9%B4%EB%A9%94%EB%9D%BC%EC%97%90%EC%84%9C-%EC%B0%8D%EC%9D%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B3%B4%EC%97%AC%EC%A3%BC%EA%B8%B0

# opencv 실행에 필요한 라이브러리 호출
import cv2

# 카메라 연결
# 프로그램 종료 시 출력되는 경고 메시지 방지를 위한 두 번쨰 아규먼트 지정
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 카메라 연결 실패 시 메시지 출력 후 프로그램 종료
if cap.isOpened() == False:
    print("Camera is not opened")
    exit(1)

# 카메라에서 얻은 이미지를 계속해서 출력하기 위한 반복문 실행
while True:
    # 카메라에서 얻은 이미지 읽어오기
    ret, img_frame = cap.read()

    # 이미지를 받아오지 못 할 경우 메시지 출력 후 반복문 탈출
    if ret == False:
        print("Capture failed")
        break

    # 이미지 좌우 반전
    img_frame = cv2.flip(img_frame, 1)
    # 얻은 이미지 Camera 윈도우를 통해 출력
    cv2.imshow('Camera', img_frame)

    # 1초 동안 키보드 입력을 기다리기
    key = cv2.waitKey(1)

    # ESC 키를 눌렀을 때 반복문 탈출
    if key == 27:
        break

cap.release()               # 카메라와 연결을 종료
cv2.destroyAllWindows()     # 모든 창 닫기