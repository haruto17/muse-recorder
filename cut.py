import cv2 as cv

def img_cut():
    img = cv.imread('image/a-1.png')

    img_b1 = img[350:800,0:600]
    cv.imwrite('image/b-1.png',img_b1)

    img_b2 = img[350:800,800:1280]
    cv.imwrite('image/b-2.png',img_b2)