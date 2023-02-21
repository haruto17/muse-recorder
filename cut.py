import cv2 as cv

def img_cut():
    img = cv.imread('a.png')

    img_b1 = img[420:700,50:550]
    cv.imwrite('b1.png',img_b1)

    img_b2 = img[350:650,800:1230]
    cv.imwrite('b2.png',img_b2)