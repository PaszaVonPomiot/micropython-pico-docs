from machine import ADC
from utime import sleep_ms

temp_sensor = ADC(4)

while True:
    adc_value = temp_sensor.read_u16()
    voltage = adc_value * (3.3 / 65535.0)
    temperature_celsius = 27 - (voltage - 0.706) / 0.001721
    print(adc_value, voltage, temperature_celsius)
    sleep_ms(100)
