# BMP280 - Pressure and temperature sensor

## Hardware
- [Raspberry Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
- [HW-611 E/P 280 sensor](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp280-ds001.pdf)  
<img src="img/bmp280-pinout.webp" alt="BMP280 Pinout" width="300">

## Software
- [MicroPython](https://micropython.org/download/RPI_PICO/) - firmware
- [pico-bmp280](https://github.com/flrrth/pico-bmp280) - sensor library

## Pinout
Schema

## Connection
Fritzing

## Functional description
### Measurement flow
1. Measure temperature
2. Measure pressure
3. Apply IIR filter (optional)
4. Save results in registers (can be read regardles of measurements)

### Power mode
- Sleep mode - no measurements performed
- Normal mode - automated, perpetual cycling between measurement and standby periods; fast readout
- Forced mode - single measurement then sleep mode; slow readout

Default: Forced mode

For low frequency measurements use forced mode.
For continuous measurements use normal mode.

### Pressure measurement
Can be disabled or oversampled up to 16x for reduced noise and better resolution.
Oversampling increases power consumption and measurement time.  
Default: 1x

### Temperature measurment
Can be disabled or oversampled up to 16x for reduced noise and better resolution.
Oversampling increases power consumption and measurement time.
Oversampling temperature makes little difference.  
Default: 1x

### IIR filter
To surpres short-term changes IIR filter can be enabled with coefficient up to 16x.  
Default: 0x

### Standby time
Determines how often automated measurements are made in normal mode. Has no effect in forced mode.  
Default: 1000 ms

## Examples

```py
# Chip configuration
chip_config = BMP280Configuration()
chip_config.power_mode = BMP280Configuration.POWER_MODE_NORMAL
chip_config.pressure_oversampling = BMP280Configuration.PRESSURE_OVERSAMPLING_16X
chip_config.temperature_oversampling = BMP280Configuration.TEMPERATURE_OVERSAMPLING_2X
chip_config.filter_coefficient = BMP280Configuration.FILTER_COEFFICIENT_OFF
chip_config.standby_time = BMP280Configuration.STANDBY_TIME__5_MS
```

```py
# Debug info
print("status", bmp280_spi.status)
print("chip_id", bmp280_spi.chip_id)
print("config", bmp280_spi.config)
print("ctrl_meas", bmp280_spi.ctrl_meas)
```

## TODO
- 
