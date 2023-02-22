import cv2 as cv
import numpy as np
import math

def perspective_transform(input_img_path,output_img_path,ratio,p1,p2,p3,p4):
    w_ratio = ratio

    img = cv.imread(input_img_path)

    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)
    p4 = np.array(p4)

    o_width = np.linalg.norm(p2-p1)
    o_width = math.floor(o_width * w_ratio)

    o_height = np.linalg.norm(p3-p1)
    o_height = math.floor(o_height)

    src = np.float32([p1,p2,p3,p4])
    dst = np.float32([[0,0],[o_width,0],[0,o_height],[o_width,o_height]])

    M = cv.getPerspectiveTransform(src,dst)

    output = cv.warpPerspective(img,M,(o_width,o_height))

    cv.imwrite(output_img_path,output)

def pers_transform():

    # music name
    perspective_transform('b1.png','name.png',1.2,[150,30],[510,160],[120,80],[495,200])

    # percentage of achievement
    perspective_transform('b1.png','achievement.png',1.2,[190,105],[300,140],[170,140],[285,175])