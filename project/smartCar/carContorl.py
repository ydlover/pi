'''
Created on 2018-2-4

@author: yudongliang
'''

import RPi.GPIO as GPIO
import time

class Car(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
    
        self.IN1 = 11
        self.IN2 = 12
        self.IN3 = 13
        self.IN4 = 15
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)

    def forward(self,continuedTime):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    def callback(self,continuedTime):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.HIGH)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    def left(self,continuedTime):
        GPIO.output(IN1,False)
        GPIO.output(IN2,False)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    def right(self,continuedTime):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,False)
        GPIO.output(IN4,False)
        time.sleep(continuedTime)
        GPIO.cleanup()


if __name__ == '__main__':
    car = Car()
    car.forward(10)
