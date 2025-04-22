# Raspberry Pi Pico


## RP2040
## Flash memory
- BOOTSEL mode lives in read-only memory and can’t be overwritten
- To clear flash memory use  [Flash Nuke UF2](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2) file

## Design considerations
- Writing to internal flash storage wears sectors that have 10k-100k write limit
    - use buffering to avoid many small writes
    - use different filenames
    - use wear leveling
