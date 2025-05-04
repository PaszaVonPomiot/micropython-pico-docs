from time import sleep

from machine import Pin

buzzer = Pin(15, mode=Pin.OUT)
buzzer.value(1)
sleep(0.3)
buzzer.value(0)
