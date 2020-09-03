from pynput.mouse import Button, Controller
import keyboard
from time import sleep
import tkinter as tk

mouse = Controller()

start = input("Press any key to start the program")

while(True):
    mouse.scroll(0,1)
    if keyboard.is_pressed("esc"):
        print("Exiting Program")
        break
    sleep(0.05)
    