import sys
import time
from random import randint

from bmp280 import BMP280SPI
from config.board import BMP280Pin
from config.sensors import get_bmp280_config
from core.base import BaseSpiGpio
from core.rtc import clock
from core.spi import spi_factory
from machine import Pin


class BMP280GPIO(BaseSpiGpio):
    SCK = Pin(BMP280Pin.SCL)
    MOSI = Pin(BMP280Pin.SDA)
    MISO = Pin(BMP280Pin.SDD)
    CS = Pin(BMP280Pin.CSB, mode=Pin.OUT, value=1)


class BMP280Sensor:
    def __init__(self) -> None:
        self.bmp280_config = get_bmp280_config()
        self.bmp280_spi = BMP280SPI(
            spi=spi_factory(spi_id=1, pinout=BMP280GPIO),
            cs=BMP280GPIO.CS,
            configuration=self.bmp280_config,
        )

    def get_readout(self) -> tuple[float, float]:
        """Get temperature and pressure readout from BMP280 sensor"""
        readout = self.bmp280_spi.measurements
        return (readout["t"], readout["p"])

    def get_csv_record(self) -> str:
        """Get a formatted CSV record with the current timestamp, temperature and pressure"""
        readout = self.bmp280_spi.measurements
        return f"{clock.now()};{readout['t']:.2f};{readout['p']:.2f}"
