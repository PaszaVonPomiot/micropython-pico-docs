"""Board configuration and pin assignment."""

from micropython import const


class Pico:
    """Pico specific configuration."""

    MCU_FREQUENCY = const(48_000_000)  # 48 MHz
    RTC_DATETIME = (2025, 5, 2, 4, 12, 0, 0, 0)  # date after reset


class BMP280Pin:
    """BMP280 to GPIO pin mapping."""

    SCL = const(10)  # SCK
    SDA = const(11)  # MOSI
    SDD = const(12)  # MISO
    CSB = const(13)  # CS
