import pyautogui
import time

for x in range(20):
    pyautogui.click()
    time.sleep(0.5)
    print('I clicked once!')