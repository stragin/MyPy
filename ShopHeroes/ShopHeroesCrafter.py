""" ShopHeroes Crafter
1) Необходимо рассчитывать координаты под разрешение экрана
    Сейчас зашиты константы под мой ноут + отступ слева из-за панельки
"""
import pyautogui as pag
import time

CraftTime = 8 # время в секундах на крафт
EasyCraft = 1 # 1 = простой крафт 0 = с прекрафтом
CellCount = 9 # Количество улучшеных ячеек

#def GetRes(x,y): # Сбор ресурсов
def GetRes(): # Сбор ресурсов
    x,y = 1870 ,210
    time.sleep(0.5)
    pag.moveTo(x,y,1)
    pag.dragTo(x,y+620,3, button='left')
def Great(x,y):
    time.sleep(0.5)
    pag.moveTo(x, y)
    pag.click()
    time.sleep(0.3)
    pag.click()

def GetCraft(x,y): #сбор крафта
    pag.moveTo(x, y, 0.5) # двигаем курсор на первую ячейку
    for i in range (CellCount):
        time.sleep(0.5)
        pag.click()
        Great(750, 950)
        x = x + 160
        pag.moveTo(x,y,0.5)

def SetCraft(x,y,wait,simple):
    pag.moveTo(x, y, 1) # двигаем курсор на первую ячейку
    pag.click()
    pag.moveTo(275,1025,1) # избранные рецепты
    pag.click()
    pag.moveTo(220,630,1) # первый рецепт
    if simple == 1: # без прекрафта
        for i in range (CellCount):
            time.sleep(0.2)
            pag.click()
    elif simple ==0: # селф прекрафт
        for i in range (CellCount):
            time.sleep(0.5)
            pag.click()
            pag.moveTo(1550, 900, 0.5)
            pag.click()
            pag.moveTo(220, 630,0.2)
   # GetRes()
    time.sleep(wait)

# favor = 275.1025
# item = 220.630
#x= 660-940
#y=920-1000
#pag.moveTo(750,950)
#print (520-360)
time.sleep(3)
#GetRes(1870,210)
#GetCraft(360,950)
#GetRes(1870,210)
for i in range (10):
    GetRes()
    SetCraft(360,950,CraftTime,EasyCraft)
    GetRes()
    GetCraft(360,950)


