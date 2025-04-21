try:
    from typing import TextIO
except ImportError:
    pass

import time

from machine import SPI, Pin

from bmp280 import BMP280SPI, BMP280Configuration

# HW-611 pinout
pin_spi1_sck = Pin(10)
pin_spi1_sda = Pin(11)
pin_spi1_sdd = Pin(12)
pin_spi1_csb = Pin(13, mode=Pin.OUT, value=1)

# BMP280 configuration is not persistent
chip_config = BMP280Configuration()
chip_config.pressure_oversampling = BMP280Configuration.PRESSURE_OVERSAMPLING_4X

# SPI configuration
spi1 = SPI(1, sck=pin_spi1_sck, mosi=pin_spi1_sda, miso=pin_spi1_sdd)
bmp280_spi = BMP280SPI(spi=spi1, cs=pin_spi1_csb, configuration=chip_config)


def get_record() -> str:
    readout = bmp280_spi.measurements
    return f"{time.time()};{readout['t']:.2f};{readout['p']:.2f}"


def save_record(file: TextIO, record: str) -> None:
    file.write(record + "\n")
    file.flush()


def measure_and_save_loop(file: TextIO) -> None:
    while True:
        record = get_record()
        print(record)
        save_record(file=file, record=record)
        time.sleep(1)


def main() -> None:
    with open("time_temp_press.csv", "a") as file:
        file.write("time_epoch;temperature_c;pressure_hpa\n")
        measure_and_save_loop(file=file)


if __name__ == "__main__":
    main()
