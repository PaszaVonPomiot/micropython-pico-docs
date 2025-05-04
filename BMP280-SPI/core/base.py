from machine import Pin


class BaseSpiGpio:
    """Interface for 4-wire SPI GPIO pins."""

    SCK: Pin  # SCK
    MOSI: Pin  # MOSI
    MISO: Pin  # MISO
    CS: Pin  # CS
