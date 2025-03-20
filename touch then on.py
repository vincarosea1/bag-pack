# Write your code here :-)
from machine import Pin, TouchPad
import time

t_pin = TouchPad(Pin(4))
red = Pin(14,Pin.OUT)


th = 250

while (True):
    t_value = t_pin.read()

    print(t_value)
    red.value(0)
    if(t_value < th):
        print("touched")
        red.value(1)
    time.sleep(0.25)

