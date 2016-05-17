#!/usr/bin/python3

import RPi.GPIO as GPIO
import time   #used for timing functions
from acunits.ac import AcUnit
GPIO.setmode(GPIO.BCM)  #set pin read mod

ac = AcUnit("AC1", 5, 75)

print(ac.getId() + " is on" if ac.isOn() else ac.getId() + " is off")




inputs = [17, 27, 22]  #setup pins to use

outputs = [5, 6, 13]

for n in inputs:
    GPIO.setup(n, GPIO.IN)

for o in outputs:
    GPIO.setup(o, GPIO.OUT)



val = [0,0,0]     #set up math fun


count = [0,0,0]  #sets counter read by indx



try:
  while True :
    
    if GPIO.input(inputs[0])==1:     
      val[0]=9    
      if sum(val)<16:
        GPIO.output(outputs[0],True)
        count[0]=time.time()
      else:
        time.sleep(6)                                         
        GPIO.input(inputs[count.index(min(count))])==0
        time.sleep(1)
        count[0]=0  
    else:    
      GPIO.output(outputs[0],False)                                     
      val[0]=0   
      count[0]=0     

    if GPIO.input(inputs[1])==1:
      val[1]=6
      if sum(val)<16:
        GPIO.output(outputs[1],True)
        count[1]=time.time()
      else:
        time.sleep(6)                                         
        GPIO.input(inputs[count.index(min(count))])==0
        time.sleep(1)
        count[1]=0  
    else:    
      GPIO.output(outputs[1],False)
      val[1]=0
      count[1]=0
      
    if GPIO.input(inputs[2])==1:
      val[2]=6
      if sum(val)<16:
        GPIO.output(outputs[2],True)
        count[2]=time.time()
      else:
      time.sleep(6)                                         
      GPIO.input(inputs[count.index(min(count))])==0
      time.sleep(1)
      count[2]=0
    else:    
      GPIO.output(outputs[2],False) 
      val[2]=0
      count[2]=0


except KeyboardInterrupt: 
  GPIO.cleanup()

