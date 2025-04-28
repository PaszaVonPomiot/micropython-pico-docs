from ds1302 import DS1302
from machine import Pin

rtc = DS1302(clk=Pin(0), dat=Pin(1), rst=Pin(2))

print(rtc.get_date_time())
