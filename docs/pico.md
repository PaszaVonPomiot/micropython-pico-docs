# Raspberry Pi Pico 1

## RP2040

https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf
https://datasheets.raspberrypi.com/rp2040/hardware-design-with-rp2040.pdf

-   CPU 133 MHz dual ARM Cortex-M0+ cores (overclockable to over 400 MHz)
-   ROM 16 KB on the RP2040 chip
    -   contains bootloader (BOOTSEL) that after reset, loads firmware from external Flash to SRAM
    -   not writable or erasable
-   SRAM 264 KB
    -   avoid duplicating variables
    -   favor generators
    -   precompile python files to mpy
    -   use gc.collect()
    -   preallocate buffer early in the program
-   Flash on-board 2 MB
    -   ~0.65 MB is used by MicroPython (~1.4MB remains)
    -   has 10k-100k sector write limit
        -   use buffering to avoid many small writes
        -   use different filenames
        -   use wear leveling
    -   QSPI interface
    -   To clear flash memory use [Flash Nuke UF2](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2) file

## Pico Board

-   Operation voltage 3.3 V
-   40 pins
    -   physical numbering 1-40 (almost never used)
    -   labeled pins (usually pin number x will mean GPx)
    -   9 ground pins (square shaped)
    -   3V3 pin - will output 3.3 V and max 300 mA
    -   VBUS pin (5V/2A)
        -   transmitts voltage directly from micro USB port (5 V)
        -   max current depends on power supply but cannot exceed 2 A
        -   use it to power 5 V peripherials
        -   VBUS will power VSYS
    -   VSYS pin
        -   supplies power to Pico
        -   generates voltage for 3V3 pin
        -   VSYS will not power VBUS
    -   GPIO pins (3.3 V/12 mA)
        -   OK for powering LED or buzzer
        -   if need to control high current device from GPIO use driver board that has separate power supply input
        -   inputs by default in a high-impedance (Hi-Z) state when not configured
-   SPI
    -   2 SPI controllers available: SPI0 and SPI1
    -   set of SPI pins has: SCK, RX, TX, CSn (SCL, MISO, MOSI, CS)
    -   SPI0 has 3 sets of pins, SPI1 has 2 sets of pins
    -   device needs to use SCL, MISO and MOSI from the same controller; CS can be any GPIO pin
-   on-board LED
-   ADC - 12-bit resolution
    -   transforms an analog signal into a value between 0 and 4095 but it's scaled to 0-65535
    -   4 ADC channels on external GPIOs
    -   GPIOs 26, 27, and 28 can be used to read output voltage from peripherals
    -   GPIO29 can measure the input voltage that powers the board (VSYS);
    -   There’s a fifth ADC channel that is connected to an internal temperature sensor.
-   PIO
    -   2 PIO coprocessors, each with 4 state machines

## Hardware design

### Power supply

-   Powering Pico
    -   through micro USB from PC or PSU (5 V)
    -   trough VBUS eg. from battery (5 V); simultaneously to micro USB can be connected only device not a PSU
    -   through VSYS (1.8 - 5.5 V)
    -   never use both sources unless you secure pins
-   Powering from Pico
    -   voltages must match
    -   max. current cannot be exceeded for Pico pin
    -   check for weakest link - Pico pin, cable, target device
