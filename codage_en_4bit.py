from machine import Pin
import time
a=Pin(21,Pin.OUT,value=0)
b=Pin(20,Pin.OUT,value=0)
c=Pin(19,Pin.OUT,value=0)
Bp=Pin(14,Pin.IN)
i=0
while(True):
    while (Bp.value()==0):
        continue
    time.sleep_ms(300)
    i=i+1
    if(i==1):
        a.off();b.off();c.on()
    elif(i==2):
        a.off();b.on();c.off()
    elif(i==3):
        a.off();b.on();c.on()
    elif(i==4):
        a.on();b.off();c.off()
    elif(i==5):
        a.on();b.off();c.on()
    elif(i==6):
        a.on();b.on();c.off()
    elif(i==7):
        a.on();b.on();c.on() 
    elif(i==8):
        a.off();b.off();c.off()
        i=0

 