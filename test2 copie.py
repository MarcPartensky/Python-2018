import pyautogui
screenWidth, screenHeight = pyautogui.size()
for y in range(screenHeight*1/3,screenHeight*2/3):
    for x in range(screenWidth*1/3,screenWidth*2/3):
        pyautogui.moveTo(x,y)
