'''
Created on 2018-1-26

@author: ydlov
'''

import RPi.GPIO as GPIO  

if __name__ == '__main__':
    pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict  
 
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
    for i in pins:  
        GPIO.setup(pins[i], GPIO.IN)   # Set pins' mode is output  
    GPIO.cleanup()  
    print("clear success!")    
    