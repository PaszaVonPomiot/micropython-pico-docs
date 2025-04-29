from bmp280_core import BMP280Logger, BMP280Loop, BMP280Sensor
from config.board import BMP280Pin
from machine import SPI, Pin


class BMP280GPIO:  # HW-611 SPI pinout
    SCL = Pin(BMP280Pin.SCL)  # SPI Clock
    SDA = Pin(BMP280Pin.SDA)  # SPI Data
    SDD = Pin(BMP280Pin.SDD)  # Additional Data Line
    CSB = Pin(BMP280Pin.CSB, mode=Pin.OUT, value=1)  # Chip Select


spi1 = SPI(1, sck=BMP280GPIO.SCL, mosi=BMP280GPIO.SDA, miso=BMP280GPIO.SDD)
sensor = BMP280Sensor(spi=spi1, cs=BMP280GPIO.CSB)
sensor_logger = BMP280Logger(sensor=sensor, buffer_size=30)
sensor_loop = BMP280Loop(logger=sensor_logger, interval_sec=1)
