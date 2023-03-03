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
    perspective_transform('image/b-1.png','image/name.png',1.1,[180,80],[535,215],[150,135],[525,250])

    # percentage of achievement
    perspective_transform('image/b-1.png','image/achievement.png',1.2,[220,155],[325,190],[200,195],[310,225])

    # max combo
    perspective_transform('image/b-1.png','image/maxcombo.png',1.2,[460,230],[520,250],[450,265],[505,280])

    # perfect num
    perspective_transform('image/b-1.png','image/perfect.png',1.2,[208,205],[285,227],[200,240],[270,260])

    # great num
    perspective_transform('image/b-1.png','image/great.png',1.2,[370,250],[450,270],[360,285],[445,305])