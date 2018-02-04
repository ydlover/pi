'''
Created on 2018-2-4

@author: yudongliang
'''
#引入gpio的模块
import RPi.GPIO as GPIO
import time
#设置GPIO模式

class Car(object):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        #设置in1到in4接口
        self.IN1 = 11
        self.IN2 = 12
        self.IN3 = 13
        self.IN4 = 15
        GPIO.setup(self.IN1,GPIO.OUT)
        GPIO.setup(self.IN2,GPIO.OUT)
        GPIO.setup(self.IN3,GPIO.OUT)
        GPIO.setup(self.IN4,GPIO.OUT)


    #前进的代码
    def forward(self,continuedTime):
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    #后退
    def callback(self,continuedTime):
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.HIGH)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    #左转
    def left(self,continuedTime):
        GPIO.output(IN1,False)
        GPIO.output(IN2,False)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        time.sleep(continuedTime)
        GPIO.cleanup()
    
    #右转
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
