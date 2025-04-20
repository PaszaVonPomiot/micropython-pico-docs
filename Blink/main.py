import utime
from machine import Pin

led = Pin("LED", mode=Pin.OUT)

while True:
    led.toggle()
    utime.sleep(0.5)
