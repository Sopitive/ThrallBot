from ctypes.wintypes import HWND
import numpy as np
import pyautogui, time, cv2, threading, queue
from win32gui import GetWindowText, GetForegroundWindow, PyGetArraySignedLong
import multiprocessing

def main():
    #Main Thread
    while True:
        global img
        window = window_handler('Destiny 2')
        if window:
            img = screenshot()
            low = health_checker()
            if low:
                left_click()
                no_afk()
#Screenshot Function to take a screenshot and save it as "screenshot.png".       
def screenshot():
    img = pyautogui.screenshot('screenshot.png')
    img = cv2.imread('screenshot.png', 1)
    return img

#Window handler function to detect if foreground (visible) window is Destiny 2. 
def window_handler(wind):
    window = GetWindowText(GetForegroundWindow())
    if window == wind:
        print("Destiny 2 Active")
        return True

def health_checker():
    # img = cv2.imread('screenshot.png', 1)
    print(img[104, 1161])
    (r, g , b) = img[104, 1161]
    if r < 200 and g < 200 and b < 200 and not b == 0:
        print('Health is low.')
        return True
    else:
        return False

def left_click():
    pyautogui.FAILSAFE = False
    for x in range(2):
        pyautogui.mouseDown(button='left')
        time.sleep(0.2)
        pyautogui.mouseUp(button='left')
        time.sleep(0.4)


def no_afk():
    pyautogui.keyDown('s')
    time.sleep(0.5)
    pyautogui.keyUp('s')
    time.sleep(2)

if __name__ == '__main__':
    main()

# while True:
#     window = GetWindowText(GetForegroundWindow())
#     if window == 'Destiny 2':
#         img = pyautogui.screenshot('screenshot.png')
#         img = cv2.imread('screenshot.png', 1)
#         print(img[104, 1161])
#         (r, g , b) = img[104, 1161]
#         if r < 200 and g < 200 and b < 200 and not b == 0:
#             # if times < 2:
#             #     pyautogui.keyDown('c')
#             #     time.sleep(0.5)
#             #     pyautogui.keyUp('c')
#             #     times += 1
#             # if times >= 2:
#             print('Health Is Low')
#             pyautogui.FAILSAFE = False
#             print(img[104, 1161])
#             for x in range(2):
#                 pyautogui.mouseDown(button='left')
#                 time.sleep(0.2)
#                 pyautogui.mouseUp(button='left')
#                 time.sleep(0.4)
#             pyautogui.keyDown('s')
#             # pyautogui.keyDown('d')
#             time.sleep(0.5)
#             pyautogui.keyUp('s')
#             # pyautogui.keyUp('d')
#         else:
#             print('Health Is Not Low')
#     else:
#         times = 0