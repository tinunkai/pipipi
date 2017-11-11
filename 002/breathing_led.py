#!/usr/bin/python
###########################################################################
#Filename      :breathing_led.py
#Description   :make breath led
#Author        :alan
#Website       :www.osoyoo.com
#Update        :2017/06/26
############################################################################

import RPi.GPIO as GPIO
import time

#set BCM_GPIO 18(GPIO1) as LED pin
LEDPIN = 17

#print message at the begining ---custom function
def print_message():
    print ('|**********************************|')
    print ('|           Breath LED             |')
    print ('|  ----------------------------    |')
    print ('|      LED Connect to GPIO1        |')
    print ('|  ----------------------------    |')
    print ('|                                  |')
    print ('|                            OSOYOO|')
    print ('|**********************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')
    pass

#setup function for some setup---custom function
def setup():
    global p
    GPIO.setwarnings(False)
    #set the gpio modes to BCM numbering
    GPIO.setmode(GPIO.BCM)
    #set all LedPin's mode to output,and initial level to HIGH(3.3V)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

    #set LEDPIN as PWM output,and frequency=100Hz
    p = GPIO.PWM(LEDPIN,100)
    #set p begin with ualue 0
    p.start(0)
    pass

#main function
def main():
    #print info
    print_message()
    while True:
        print("|****************************|")
        print("|    Increase duty cycle     |")
        print("|****************************|")
        #increase duty cycle from 0 to 100
        for dc in range(0,101,4):
            #chang duty cycle to dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            pass
        print("|****************************|")
        print("|    Decrease duty cycle     |")
        print("|****************************|")
        #decrease duty cycle from 100 to 0
        for dc in range(100,-1,-4):
            #change duty cycle to dc
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            pass
        pass
    pass

#define a destroy function for clean up everything after the script finished
def destroy():
    #stop p
    p.stop()
    #turn off led
    GPIO.output(LEDPIN,GPIO.LOW)
    #release resource
    GPIO.cleanup()
    pass

# if run this script directly ,do:
if __name__ == '__main__':
    setup()
    try:
            main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()
        pass
    pass
