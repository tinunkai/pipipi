#!/usr/bin/python

import RPi.GPIO as GPIO
import time

LEDPIN = 17

def setup():
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

    p = GPIO.PWM(LEDPIN,100)
    p.start(0)

def main():
    while True:
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

def destroy():
    p.stop()
    GPIO.output(LEDPIN,GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
            main()
    except KeyboardInterrupt:
        destroy()

