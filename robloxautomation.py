import time
import win32com.client as comclt
import ctypes
from ctypes import wintypes
import pyautogui
import random

random.seed()

# wsh = comclt.Dispatch('WScript.Shell')
# wsh.AppActivate("Roblox")

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def AltTab():
    """Press Alt+Tab and hold Alt key for 2 seconds
    in order to see the overlay.
    """
    PressKey(VK_MENU)   # Alt
    PressKey(VK_TAB)    # Tab
    ReleaseKey(VK_TAB)  # Tab~
    time.sleep(2)
    ReleaseKey(VK_MENU) # Alt~

# if __name__ == "__main__":
#     AltTab()

def GoUp(duration):
    print("pressing the [up] key")
    PressKey(0x57)
    time.sleep(duration)
    ReleaseKey(0x57)

def GoDown(duration):
    print("pressing the [down] key")
    PressKey(0x53)
    time.sleep(duration)
    ReleaseKey(0x53)

def GoLeft(duration):
    print("pressing the [left] key")
    PressKey(0x41)
    time.sleep(duration)
    ReleaseKey(0x41)

def GoRight(duration):
    print("pressing the [right] key")
    PressKey(0x44)
    time.sleep(duration)
    PressKey(0x44)

def Jump(duration):
    print("pressing the [space] key")
    PressKey(0x20)
    time.sleep(duration)
    ReleaseKey(0x20)

def Click(duration):
    pyautogui.click(None, None, 5, 1.1, 'left', duration)

def OpenRoblox():
    wsh = comclt.Dispatch('WScript.Shell')
    wsh.AppActivate("Roblox")

def RandomTime(floor, ceiling):
    return random.randint(floor, ceiling)
# for x in range(0,5):
#     # print("pressing the [space] key")
#     # PressKey(0x20)
#     # time.sleep(1)
#     # ReleaseKey(0x20)
#     # print("pressing the [up] key")
#     # PressKey(0x57)
#     # time.sleep(1)
#     # ReleaseKey(0x57)
#     GoUp(1)
#     Jump(1)
#     GoDown(1)
#     Jump(1)
#     GoLeft(1)
#     Jump(1)
#     GoRight(1)
#     # print("pressing the [down] key")
#     # PressKey(0x53)
#     # time.sleep(1)
#     # ReleaseKey(0x53)
#     # print("pressing the [left] key")
#     # PressKey(0x41)
#     # time.sleep(1)
#     # ReleaseKey(0x41)
#     # print("pressing the [right] key")
#     # PressKey(0x44)
#     # time.sleep(1)
#     # PressKey(0x44)
#     x += 1