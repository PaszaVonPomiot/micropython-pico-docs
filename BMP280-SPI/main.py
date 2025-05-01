"""
Set correct SensorLogger.buffer to avoid MemoryError (buffer~183 seems to be max from host, but from Pico buffer~???)
"""

from core.bmp280 import BMP280Sensor


def main():
    sensor = BMP280Sensor()
    print(sensor.get_csv_record())
    print(sensor.get_readout())
    print(sensor.get_csv_record())


if __name__ == "__main__":
    main()
