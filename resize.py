import cv2 as cv

resolution = 1280 * 720

def img_resize():
    img = cv.imread('image/a1.png')

    h,w = img.shape[:2]
    scale = (resolution / (w * h)) ** 0.5
    img_resize = cv.resize(img, dsize=None,fx=scale,fy=scale)

    