"""
Set correct SensorLogger.buffer to avoid MemoryError (buffer~183 seems to be max from host, but from Pico buffer~???)
"""

from setup import sensor_loop


def main():
    sensor_loop.start()


if __name__ == "__main__":
    main()
