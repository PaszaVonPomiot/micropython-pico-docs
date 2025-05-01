from micropython import const


class Pico:
    """Pico board specific settings"""

    MCU_FREQUENCY = const(48_000_000)  # 48 MHz
    RTC_DATETIME = (2025, 5, 2, 4, 12, 0, 0, 0)


class BMP280Pin:
    """Pin names on BMP280"""

    SCL = const(10)  # SCK
    SDA = const(11)  # MOSI
    SDD = const(12)  # MISO
    CSB = const(13)  # CS
