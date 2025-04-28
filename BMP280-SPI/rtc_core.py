"""
Placeholdr module for RTC core functionality.
"""

import time


class Clock:
    @staticmethod
    def get_timestamp():  # TODO: should return "YYYY-MM-DD HH:MM:SS"
        return time.ticks_ms() // 1000
