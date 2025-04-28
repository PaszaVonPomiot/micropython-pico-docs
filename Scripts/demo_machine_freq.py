"""
freq(MCU_frequency[, peripheral_frequency=48_000_000])
MCU frequency at boot time resets to 125 MHz. Can be changed between 48 MHz to about 250 MHz.
MCU frequency at boot time resets to 125 MHz. Can be changed to 48 MHz.
"""

from machine import freq

print(freq())
freq(48000000)  # MCU 48 kHz
print(freq())
freq(240000000)
print(freq())
freq(125000000, 48000000)  # UART 48 kHz
print(freq())
