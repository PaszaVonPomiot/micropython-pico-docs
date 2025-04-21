try:
    from typing import TextIO
except ImportError:
    pass  # For MicroPython compatibility

import os
import time

from machine import SPI, Pin

from bmp280 import BMP280SPI, BMP280Configuration


class Spi1Pin:  # HW-611 pinout
    SCL = Pin(10)  # SPI Clock
    SDA = Pin(11)  # SPI Data
    SDD = Pin(12)  # Additional Data Line
    CSB = Pin(13, mode=Pin.OUT, value=1)  # Chip Select Bar


# SPI configuration
spi1 = SPI(1, sck=Spi1Pin.SCL, mosi=Spi1Pin.SDA, miso=Spi1Pin.SDD)


class Sensor:
    def __init__(
        self, spi: SPI, cs: Pin, config: BMP280Configuration | None = None
    ) -> None:
        self.bmp280_config = self._get_config(config=config)
        self.bmp280_spi = BMP280SPI(spi=spi, cs=cs, configuration=self.bmp280_config)

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
        return f"{time.time()};{readout['t']:.2f};{readout['p']:.2f}"


class SensorLogger:
    def __init__(self, sensor: Sensor) -> None:
        self.file_name = f"{time.time()}.csv"
        self.folder_name = "data"
        self.file_path = f"{self.folder_name}/{self.file_name}"
        self.buffer: list[str] = []
        self.sensor = sensor
        self._data_folder_setup()
        self._file_setup()

    def _data_folder_setup(self):
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
            file.write("epoch;temp_c;pres_hpa\n")

    def save_record_to_buffer(self) -> None:
        """Buffer readings to reduce flash wear"""
        record = self.sensor.get_record()
        self.buffer.append(record)

    def serialize_buffer(self) -> str:
        buffer_serialized = "\n".join(self.buffer) + "\n"
        self.buffer.clear()
        return buffer_serialized

    def save_buffer_to_file(self, min_items: int) -> None:
        if not self.buffer_ready_to_flush(min_items=min_items):
            return
        serialized_buffer = self.serialize_buffer()
        with open(self.file_path, mode="a") as file:
            file.write(serialized_buffer)

    def buffer_ready_to_flush(self, min_items: int) -> bool:
        return len(self.buffer) >= min_items


class SensorLoop:
    def __init__(self, logger: SensorLogger, interval_sec: float = 1.0) -> None:
        self.logger = logger
        self.interval_sec = interval_sec
        self._running = False

    def start(self) -> None:
        self._running = True
        while self._running:
            self.logger.save_record_to_buffer()
            self.logger.save_buffer_to_file(min_items=3600)
            time.sleep(self.interval_sec)

    def stop(self) -> None:
        self._running = False


def main() -> None:
    sensor = Sensor(spi=spi1, cs=Spi1Pin.CSB)
    sensor_logger = SensorLogger(sensor=sensor)
    sensor_loop = SensorLoop(logger=sensor_logger)
    sensor_loop.start()


if __name__ == "__main__":
    main()
