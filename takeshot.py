import pyautogui as ag
import pygetwindow as gw
from time import sleep

def takescreenshot():
    muse = gw.getWindowsWithTitle('MuseDash')[0]

    muse.activate()
    x,y=muse.topleft
    width,height=muse.size

    sleep(1)
    screenshot=ag.screenshot('image/a-1.png',region=(x,y,width,height))