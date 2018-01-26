'''
Created on 2018��1��26��

@author: ydlov
'''

import RPi.GPIO as GPIO  
import time  
  
def map(x, in_min, in_max, out_min, out_max):   # ��һ������һ����������ӳ�䵽��һ�����䣬���罫0~100֮���һ����ӳ�䵽0~255֮��  
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min  
  
def setColor(col):   # For example : col = 0x112233  
    R_val = (col & 0xFF0000) >> 16  
    G_val = (col & 0x00FF00) >> 8  
    B_val = (col & 0x0000FF) >> 0  
      
    R_val = map(R_val, 0, 255, 0, 100)   # change a num(0~255) to 0~100.  
    G_val = map(G_val, 0, 255, 0, 100)  
    B_val = map(B_val, 0, 255, 0, 100)  
      
    p_R.ChangeDutyCycle(100 - R_val)     # Change duty cycle  
    p_G.ChangeDutyCycle(100 - G_val)  
    p_B.ChangeDutyCycle(100 - B_val)  
  
try:  
    while True:  
        for col in colors:  
            setColor(col)  
            time.sleep(0.5)  
except KeyboardInterrupt:  
    p_R.stop()  
    p_G.stop()  
    p_B.stop()  
    for i in pins:  
        GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds  
    GPIO.cleanup()  
    
if __name__ == '__main__':
    
    colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0xFFFFFF, 0x9400D3]  
    pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict  
      
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location  
    for i in pins:  
        GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output  
        GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led  
      
    p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz  
    p_G = GPIO.PWM(pins['pin_G'], 2000)  
    p_B = GPIO.PWM(pins['pin_B'], 5000)  
      
    p_R.start(100)      # Initial duty Cycle = 100(leds off)  
    p_G.start(100)  
    p_B.start(100)  
  
    