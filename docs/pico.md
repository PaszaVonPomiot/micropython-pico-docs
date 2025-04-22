# Raspberry Pi Pico
## Design considerations
- Writing to internal flash storage wears sectors that have 10k-100k write limit
    - use buffering to avoid many small writes
    - use different filenames
    - use wear leveling
