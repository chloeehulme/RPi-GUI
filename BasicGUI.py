"""
   A basic GUI that toggles 3 LED's on and off.
   Uses:  RPi model 3, Red LED, Green LED, Blue LED
   Author: Chloe Hulme
"""

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

# hardware
led_red = LED(15)
led_green = LED(23)
led_blue = LED(24)

# GUI definitions
win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")


# event functions
# Turns off red LED if already on, else turns on red LED, turns off all other LED's
def toggle_red():
    if led_red.is_lit:
        led_red.off()
        ledButtonRed["text"] = "Turn LED On"
    else:
        led_green.off()
        led_blue.off()
        led_red.on()
        ledButtonRed["text"] = "Turn LED Off"
        ledButtonGreen["text"] = "Turn LED On"
        ledButtonBlue["text"] = "Turn LED On"


# Turns off green LED if already on, else turns on green LED, turns off all other LED's
def toggle_green():
    if led_green.is_lit:
        led_green.off()
        ledButtonGreen["text"] = "Turn LED On"
    else:
        led_red.off()
        led_blue.off()
        led_green.on()
        ledButtonGreen["text"] = "Turn LED Off"
        ledButtonRed["text"] = "Turn LED On"
        ledButtonBlue["text"] = "Turn LED On"


# Turns off blue LED if already on, else turns on blue LED, turns off all other LED's
def toggle_blue():
    if led_blue.is_lit:
        led_blue.off()
        ledButtonBlue["text"] = "Turn LED On"
    else:
        led_red.off()
        led_green.off()
        led_blue.on()
        ledButtonBlue["text"] = "Turn LED Off"
        ledButtonRed["text"] = "Turn LED On"
        ledButtonGreen["text"] = "Turn LED On"


# closes window
def close():
    RPi.GPIO.cleanup()
    win.destroy()


# create widgets
ledButtonRed = Button(win, text='Turn LED On', font=myFont, command=toggle_red, bg='IndianRed1', height=1, width=24)
ledButtonGreen = Button(win, text='Turn LED On', font=myFont, command=toggle_green, bg='PaleGreen1', height=1, width=24)
ledButtonBlue = Button(win, text='Turn LED On', font=myFont, command=toggle_blue, bg='CadetBlue1', height=1, width=24)

# positions widgets
ledButtonRed.grid(row=0, column=1)
ledButtonGreen.grid(row=1, column=1)
ledButtonBlue.grid(row=2, column=1)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='seashell1', height=1, width=6)
exitButton.grid(row=3, column=4)

# link top RHS x to close function
win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()

