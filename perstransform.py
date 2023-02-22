import cv2 as cv
import numpy as np
import math

def perspective_transform():
    w_ratio = 1.2

    p1 = np.array([150,30])
    p2 = np.array([490,150])
    p3 = np.array([120,85])
    p4 = np.array([480,200])

    img = cv.imread('b1.png')

    o_width = np.linalg.norm(p2-p1)
    o_width = math.floor(o_width * w_ratio)

    o_height = np.linalg.norm(p3-p1)
    o_height = math.floor(o_height)

    src = np.float32([p1,p2,p3,p4])
    dst = np.float32([[0,0],[o_width,0],[0,o_height],[o_width,o_height]])

    M = cv.getPerspectiveTransform(src,dst)

    output = cv.warpPerspective(img,M,(o_width,o_height))

    cv.imwrite('name.png',output)
