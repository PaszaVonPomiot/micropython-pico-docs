import machine

# Returns to 125000000 Hz after reset
print(machine.freq())
machine.freq(48000000)  # CPU 48 MHz
print(machine.freq())
machine.freq(240000000)
print(machine.freq())
machine.freq(125000000, 125000000)  # UART 125 kHz
print(machine.freq())
