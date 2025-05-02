import sys

if sys.implementation.name != "micropython":
    from typing import Literal

from core.base import BaseSpiGpio
from machine import SPI


def spi_factory(spi_id: Literal[0, 1], pinout: type[BaseSpiGpio]) -> SPI:
    """Ensure the correct SPI controller is matched with correct GPIO pins."""
    return SPI(spi_id, sck=pinout.SCK, mosi=pinout.MOSI, miso=pinout.MISO)
