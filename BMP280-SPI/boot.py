import time

import machine
from config.board import Pico

time.sleep(2)
machine.freq(Pico.MCU_FREQUENCY)
machine.RTC().datetime(Pico.RTC_DATETIME)  # sync internal RTC
