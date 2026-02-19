import keyboard
import win32api, win32con
import time
import ctypes
import mouse

from ctypes import windll #new

timeBeginPeriod = windll.winmm.timeBeginPeriod #new
timeBeginPeriod(1)

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
center_x = int(screensize[0] / 2)
center_y = int(screensize[1] / 2)

pixels = 80
cursor = -1

while True:

    flagStart = 1

    while mouse.is_pressed('left'):
        counter = 0

        while counter < int(pixels / (flagStart + 1)):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 1*cursor, 0, 0, 0)
            counter += 1
            time.sleep(0.0006)

        flagStart = 0
        cursor = cursor*-1

    time.sleep(0.01)