import cv2 as cv
import numpy as np

def getpos():
    img = cv.imread('image/b-2.png')

    def click_pos(event,x,y,flags,params):
        if event == cv.EVENT_LBUTTONDOWN:
            img2 = np.copy(img)
            cv.circle(img2,center=(x,y),radius=5,color=255,thickness=-1)
            pos_str='(x,y)=('+str(x)+','+str(y)+')'
            cv.putText(img2,pos_str,(x+10, y+10),cv.FONT_HERSHEY_PLAIN,2,255,2,cv.LINE_AA)
            cv.imshow('window', img2)
            print(x,y)
    cv.imshow('window',img)
    cv.setMouseCallback('window',click_pos)
    cv.waitKey(0)
    cv.destroyAllWindows()