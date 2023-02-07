import pyautogui
import time

thing = str(input("enter da thing: "))
delay = float(input("Enter delay time: "))

while True:
    pyautogui.typewrite(thing)
    pyautogui.press("Enter")
    time.sleep(delay)