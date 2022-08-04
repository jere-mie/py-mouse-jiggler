#!/usr/bin/python3
try:
    import pyautogui
except ImportError:
    print("pyautogui not installed - install it by running 'python3 -m pip install pyautogui' and re-run")
    exit(1)
import time
while True:
    pyautogui.dragTo(100, 100)
    time.sleep(0.5)
    pyautogui.dragTo(200, 200)
    time.sleep(0.5)
