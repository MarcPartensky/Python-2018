#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        print((x,y))

except KeyboardInterrupt:
    print('\n')
