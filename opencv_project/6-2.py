# 블렌딩

import cv2

alpha = 0.0     # 0에 가까우면 투명
beta = 1.0      # 1에 가까우면 불투명

img1 = cv2.imread("paper.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("gradation.png", cv2.IMREAD_COLOR)

# 블렌딩을 하기 위해서는 이미지 크기가 같아야 함. 이미지 크기 조정 작업!
re_img1 = cv2.resize(img1, dsize=(480, 640), interpolation=cv2.INTER_AREA)
re_img2 = cv2.resize(img2, dsize=(480, 640), interpolation=cv2.INTER_AREA)

# 이미지 크기 원하는대로 조정되었는지 확인
img_result = cv2.hconcat([re_img1, re_img2])
cv2.imshow("result", img_result)
cv2.waitKey(0)

while alpha <= 1.0:
    img1 = re_img1
    img2 = re_img2

    # 감마값을 올릴 수록 이미지는 밝아짐!
    dst = cv2.addWeighted(img1, alpha, img2, beta, 0)

    print(alpha, "", beta)

    cv2.imshow("dst", dst)
    key = cv2.waitKey(0)

    if key == ord('1'):   # 1번 누르면 사진 촬영됨
        cv2.imwrite('document.jpg', dst) # 사진 저장

    alpha = round(alpha + 0.1, 1)
    beta = round(beta - 0.1, 1)

cv2.destroyAllWindows()