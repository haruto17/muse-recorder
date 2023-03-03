import cv2 as cv

def img_threshold():
    img = cv.imread("image/great.png")
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, img2 = cv.threshold(img_gray, 0, 255, cv.THRESH_OTSU)

    cv.imwrite("th.png",img2)