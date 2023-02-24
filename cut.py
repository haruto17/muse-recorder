import cv2 as cv

def img_cut():
    img = cv.imread('image/a-1.png')

    img_b1 = img[400:700,30:550]
    cv.imwrite('image/b-1.png',img_b1)

    img_b2 = img[350:650,800:1230]
    cv.imwrite('image/b-2.png',img_b2)