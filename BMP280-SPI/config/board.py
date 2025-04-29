from micropython import const


class Pico:
    MCU_FREQUENCY = const(48 * 1000000)  # 48 MHz


class BMP280Pin:  # HW-611 SPI pinout
    SCL = const(10)  # SCK pin for SPI
    SDA = const(11)  # MOSI pin for SPI
    SDD = const(12)  # MISO pin for SPI
    CSB = const(13)  # CS pin for SPI
