import time

from machine import freq, reset_cause


def delay_execution(seconds: int) -> None:
    """
    For development purposes wait so that MicroPico have time to
    auto-connect with vREPL and prevent main() from execution.
    """
    time.sleep(seconds)


def mcu_setup(mhz: int = 48) -> None:
    freq(mhz * 1000000)
    print(f"MCU frequency: {freq() // 1000000} MHz")
    print(f"Uptime: {time.ticks_ms() // 1000}s")
    print("Reset cause: ", reset_cause())
    delay_execution(seconds=2)
