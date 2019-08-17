""" version 1.0
future: without external modules
"""

import pyautogui, time
while True:
    x, y = pyautogui.position()
    if x+y>0:
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end ='')
        time.sleep(0.1)
        print('\b' * len(positionStr), end='')
    else:
        break