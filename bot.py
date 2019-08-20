from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (520,380)
    dinasaur = (291,395)#378 #395 17
def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Cordinates.dinasaur[0]+60,Cordinates.dinasaur[1],
           Cordinates.dinasaur[0]+150,Cordinates.dinasaur[1]+6)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())

def main():
    restartGame()
    while True:
        if (imageGrab() !=787):
            pressSpace()
            time.sleep(0.1)

main()

#restartGame()
#time.sleep(1)
#pressSpace()