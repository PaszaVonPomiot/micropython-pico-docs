import time

import machine
from config.board import Pico

time.sleep(2)
machine.freq(Pico.MCU_FREQUENCY)

rtc = machine.RTC()
rtc.datetime((2024, 4, 30, None, 2, 5, 20, None))
print("boot complete at", rtc.datetime())
