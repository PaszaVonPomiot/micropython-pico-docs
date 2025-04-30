import os
import sys
import time
from random import randint

from bmp280 import BMP280SPI, BMP280Configuration
from config.board import BMP280Pin
from core.base import BaseSpiGpio
from core.rtc import Clock
from core.spi import spi_factory
from machine import Pin


class BMP280GPIO(BaseSpiGpio):
    SCK = Pin(BMP280Pin.SCL)
    MOSI = Pin(BMP280Pin.SDA)
    MISO = Pin(BMP280Pin.SDD)
    CS = Pin(BMP280Pin.CSB, mode=Pin.OUT, value=1)


class BMP280Sensor:
    def __init__(
        self,
        config: BMP280Configuration | None = None,
    ) -> None:
        self.bmp280_config = self._get_config(config=config)
        self.bmp280_spi = BMP280SPI(
            spi=spi_factory(spi_id=1, pinout=BMP280GPIO),
            cs=BMP280GPIO.CS,
            configuration=self.bmp280_config,
        )

    def _get_config(self, config: BMP280Configuration | None) -> BMP280Configuration:
        if config is None:
            return self._default_config()
        else:
            return config

    def _default_config(self) -> BMP280Configuration:
        config = BMP280Configuration()
        config.pressure_oversampling = BMP280Configuration.PRESSURE_OVERSAMPLING_4X
        return config

    def get_record(self) -> str:
        readout = self.bmp280_spi.measurements
        return f"{Clock.get_timestamp()};{readout['t']:.2f};{readout['p']:.2f}"


class BMP280Logger:
    def __init__(self, buffer_size: int = 60) -> None:
        self.file_name = self._get_random_file_name()
        self.folder_name = "data"
        self.file_path = f"{self.folder_name}/{self.file_name}"
        self.buffer: list[str] = []
        self.buffer_size = buffer_size
        self._data_folder_setup()
        self._file_setup()

    def _get_random_file_name(self) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        name = "".join(chars[randint(0, 25)] for _ in range(8))
        return f"{name}.csv"

    def _data_folder_setup(self) -> None:
        try:
            os.mkdir(self.folder_name)
        except OSError:
            pass

    def _file_setup(self) -> None:
        if self._file_exists():
            return
        else:
            self._create_new_file()

    def _file_exists(self) -> bool:
        try:
            os.stat(self.file_path)
        except OSError:
            return False
        return True

    def _create_new_file(self) -> None:
        with open(self.file_path, mode="w") as file:
            file.write("uptime_s;temperature_c;pressure_hpa\n")

    def add_record_to_buffer(self, record: str) -> None:
        """Use buffer to reduce flash wear"""
        # record = self.sensor.get_record()
        print(record)
        self.buffer.append(record)

    def serialize_buffer(self) -> str:
        buffer_serialized = "\n".join(self.buffer) + "\n"
        self.buffer.clear()
        return buffer_serialized

    def save_buffer_to_file(self) -> None:
        serialized_buffer = self.serialize_buffer()
        with open(self.file_path, mode="a") as file:
            file.write(serialized_buffer)

    def buffer_full(self) -> bool:
        return len(self.buffer) >= self.buffer_size


# class BMP280Loop:
#     def __init__(self, logger: BMP280Logger, interval_sec: float = 1.0) -> None:
#         self.logger = logger
#         self.interval_sec = interval_sec
#         self._running = False

#     def start(self) -> None:
#         self._running = True
#         self.loop()

#     def loop(self):
#         while self._running:
#             try:
#                 self.logger.add_record_to_buffer()
#                 if self.logger.buffer_full():
#                     self.logger.save_buffer_to_file()
#             except MemoryError as error:
#                 with open("error.log", "w") as file:
#                     sys.print_exception(error, file)
#             time.sleep(self.interval_sec)

#     def stop(self) -> None:
#         self._running = False


# sensor_logger = BMP280Logger(buffer_size=30)
