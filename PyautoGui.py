import pyautogui
import os

os.chdir("/Users/olivierpartensky/Desktop/")
#a=pyautogui.locateOnScreen('looksLikeThis.png')
a=pyautogui.locateCenterOnScreen('looksLikeThis.png',grayscale=True)
print(a)
