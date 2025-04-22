import time

from machine import Pin

led = Pin("LED", mode=Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
