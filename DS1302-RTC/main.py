from ds1302 import DS1302
from machine import Pin

rtc = DS1302(clk=Pin(0), dat=Pin(1), rst=Pin(2))
# rtc.set_date_time([2025, 5, 1, 4, 22, 36, 30])
print(rtc.get_date_time())
