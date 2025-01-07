from machine import Pin
import time
led=Pin(21,Pin.OUT,value=0)
Bp=Pin(14,Pin.IN)

while(True):
    while(Bp.value()==0):
        continue
    for i in range(3):
        time.sleep_ms(500)
        led.on()
        time.sleep_ms(500)
        led.off()
    while(Bp.value()==0):
        continue      
    for i in range(6):
        time.sleep_ms(250)
        led.on()
        time.sleep_ms(250)
        led.off()
    while(Bp.value()==0):
        continue      
    for i in range(12):
        time.sleep_ms(125)
        led.on()
        time.sleep_ms(125)
        led.off()
    while(Bp.value()==0):
        continue     
    for i in range(24):
        time.sleep_ms(62)
        led.on()
        time.sleep_ms(63)
        led.off()
    while(Bp.value()==0):
        continue