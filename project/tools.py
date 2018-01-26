'''
Created on 2018-1-26

@author: ydlov
'''

import RPi.GPIO as GPIO  

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
    GPIO.cleanup()  
    print("clear success!")    
    