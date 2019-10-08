import pyautogui
import time
import ctypes
from ctypes import wintypes
# import win32com.client as comclt

print("click and move")
print("author: chris case")

time.sleep(5)
pyautogui.click(None,None,1,0.0,'left',10)
# wsh = comclt.Dispatch('WScript.Shell')
# wsh.AppActivate("Roblox")
# for x in range(0, 100):
#     wsh.SendKeys("w")
# print('holding down [left] key for 5 seconds')

# for x in range(0, 10):
#     print("clicking left")
#     pyautogui.keyDown('space')
#     time.sleep(10)
#     pyautogui.keyUp('space')
    # pyautogui.press(['space', 'space', 'space', 'space'], 10, 2.0, 1.0)
# pyautogui.click(None,None,1,0.0,'left',10)
# pyautogui.press('s',10)
# pyautogui.click(None,None,1,0.0,'left',10)
# pyautogui.press('a',10)
# pyautogui.click(None,None,1,0.0,'left',10)
# pyautogui.press('d',10)


def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


print("script complete")