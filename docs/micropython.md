# MicroPython

MicroPython implements Python 3.4 with selected features from later versions

## REPL

-   Auto-indent - after `RETURN`
-   Auto-completion - with `TAB`
-   Interrupting a running program - with `Ctrl-C` if program doesn't intercept `KeyboardInterrupt`
-   Paste mode - use `Ctrl-E`, paste, then `Ctrl-D`
-   Soft reset
    -   will reset interpreter except connection to the board
    -   `Ctrl-D` OR `machine.soft_reset()`
-   Raw mode and Raw-paste mode
    -   Raw mode (`Ctrl-A`) - for programatic use, no echo
    -   Raw-paste mode (Entered from raw mode using `b"\x05A\x01"`) offers flow control and memory efficiency for high-speed transfers

## Reset and Boot Sequence

## MicroPython remote control: mpremote

## MicroPython .mpy files

## Writing interrupt handlers

## Maximising MicroPython speed

## MicroPython on microcontrollers

## MicroPython manifest files

## Package management

## Inline assembler for Thumb2 architectures

## Working with filesystems

## The pyboard.py tool

## MicroPython 2.0 Migration Guide

---

-   I2C
-   SoftI2C
-   I2S
-   SoftI2S
-   UART
-   RTC
-   Signal
-   Timer
