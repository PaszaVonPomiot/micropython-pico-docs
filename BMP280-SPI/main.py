"""
Set correct SensorLogger.buffer to avoid MemoryError (buffer~183 seems to be max from host, but from Pico buffer~???)
"""

from setup import sensor_loop
from utils import mcu_setup


def main():
    # bmp280sensor.loop.start() # should be that simple
    sensor_loop.start()


if __name__ == "__main__":
    mcu_setup()
    main()
