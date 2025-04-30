from micropython import const


class Pico:
    MCU_FREQUENCY = const(48_000_000)  # 48 MHz


class BMP280Pin:
    """Pin names on BMP280"""

    SCL = const(10)  # SCK
    SDA = const(11)  # MOSI
    SDD = const(12)  # MISO
    CSB = const(13)  # CS
