def F1(a=int(),b=int()):
    return a*b
def F2(a=int(),b=int()):
    if (a==1) or (b==1) : return 1
    else : return a+b
    
def F3(a=int(),b=int()):
    if a==b : return 1
    elif a!=b : return 0
    
from machine import Pin
led3=Pin(20,Pin.OUT,value=0)
led2=Pin(19,Pin.OUT,value=0)
led1=Pin(18,Pin.OUT,value=0)
Bp1=Pin(14,Pin.IN)
Bp2=Pin(15,Pin.IN)

while True :
    
    led1.value(F1(Bp1.value(),Bp2.value()))
    led2.value(F2(Bp1.value(),Bp2.value()))
    led3.value(F3(Bp1.value(),Bp2.value()))
    


    
    
