import cv2 as cv
import numpy as np   
import random       

# 마우스 버튼 눌렸는지 확인
mouse_is_pressing = False
# True면 사각형, False면 원 그리기
drawing_mode = True       
start_x, start_y = -1, -1   
color = (255, 255, 255)   
# 그림 그릴 캔버스 크기 지정
img = np.zeros((512, 512, 3), np.uint8) 

def mouse_callback(event,x,y,flags,param):

    global color, start_x, start_y, drawing_mode, mouse_is_pressing

    if event == cv.EVENT_MOUSEMOVE: 

        if mouse_is_pressing == True: 
            # -1의 의미는 색을 채운다는 것.
            if drawing_mode == True: 
                cv.rectangle(img,(start_x,start_y), (x,y), color, -1)
            else:
                cv.circle(img, (start_x,start_y), max(abs(start_x - x), abs(start_y - y)), color, -1)


    elif event == cv.EVENT_LBUTTONDOWN:
        color = (random.randrange(256), random.randrange(256), random.randrange(256)) 
        mouse_is_pressing = True      
        start_x, start_y = x, y     


    elif event == cv.EVENT_LBUTTONUP: 
        mouse_is_pressing = False      

        if drawing_mode == True:  
            cv.rectangle(img,(start_x,start_y),(x,y),color,-1)
        else:
            cv.circle(img, (start_x,start_y), max(abs(start_x - x), 
                abs(start_y - y)), color, -1)


    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_mode = 1 - drawing_mode


cv.namedWindow('image')   
cv.setMouseCallback('image', mouse_callback) 


while(1):

    cv.imshow('image',img)

    key = cv.waitKey(1)
    if key == 27: 
        break

cv.destroyAllWindows() 
