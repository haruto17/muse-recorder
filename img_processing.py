import cv2 as cv

resolution = 1280 * 720

def img_processing():
    img = cv.imread('a.png')

    h,w = img.shape[:2]
    scale = (resolution / (w * h)) ** 0.5
    img_resize = cv.resize(img, dsize=None,fx=scale,fy=scale)
    cv.imshow("resize_img",img_resize)
    cv.waitKey(0)
    print(img_resize.shape)