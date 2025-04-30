import time


class Clock:
    @staticmethod
    def sync_rtc() -> None:
        """Sync internal RTC with external RTC."""
        ...

    @staticmethod
    def get_timestamp():  # TODO: should return "YYYY-MM-DD HH:MM:SS"
        return time.ticks_ms() // 1000
