from machine import SPI, Pin
from machine import freq

Pin(2, Pin.OUT)


print(freq())
freq(48000000)  # MCU 48 kHz
print(freq())
freq(240000000)
print(freq())
freq(125000000, 48000000)  # UART 48 kHz
print(freq())