import cv2 as cv

path_list = ["name.png","achievement.png","maxcombo.png","perfect.png","great.png","pass.png","miss.png","score.png"]

def img_threshold():
    for item in path_list:
        img = cv.imread("image/" + item)
        img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        ret, img2 = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
        cv.imwrite("image/" + item,img2)