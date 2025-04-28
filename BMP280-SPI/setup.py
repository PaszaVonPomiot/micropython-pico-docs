from bmp280_core import BMP280Logger, BMP280Loop, BMP280Pinout, BMP280Sensor
from machine import SPI

spi1 = SPI(1, sck=BMP280Pinout.SCL, mosi=BMP280Pinout.SDA, miso=BMP280Pinout.SDD)
sensor = BMP280Sensor(spi=spi1, cs=BMP280Pinout.CSB)
sensor_logger = BMP280Logger(sensor=sensor, buffer_size=180)
sensor_loop = BMP280Loop(logger=sensor_logger, interval_sec=1)
