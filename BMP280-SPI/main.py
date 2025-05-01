import time

from core.bmp280 import BMP280Sensor
from core.logger import LoggerCSV


def main():
    sensor = BMP280Sensor()
    logger = LoggerCSV(
        file_name="bmp280.csv",
        csv_headers=["timestamp", "temperature", "pressure"],
        buffer_size=180,
    )

    while True:
        logger.process_record(record=sensor.get_csv_record())
        time.sleep(10.0)


if __name__ == "__main__":
    main()
