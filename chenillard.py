from machine import Pin
import time
led4=Pin(21,Pin.OUT,value=0)
led3=Pin(20,Pin.OUT,value=0)
led2=Pin(19,Pin.OUT,value=0)
led1=Pin(18,Pin.OUT,value=0)
Bp=Pin(14,Pin.IN)
while(1):
    while True:
        led4.on()
        time.sleep_ms(400)
        led3.on()
        led4.off()
        time.sleep_ms(400)
        led2.on()
        led3.off()
        time.sleep_ms(400)
        led1.on()
        led2.off()
        time.sleep_ms(400)
        led1.off()
        if(Bp.value()==1):
            break
    
  
    while True:
        led1.on()
        time.sleep_ms(400)
        led2.on()
        led1.off()
        time.sleep_ms(400)
        led3.on()
        led2.off()
        time.sleep_ms(400)
        led4.on()
        led3.off()
        time.sleep_ms(400)
        led4.off()
        if(Bp.value()==1):
            break
        