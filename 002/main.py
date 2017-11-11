#!/usr/bin/python

import RPi.GPIO as GPIO
import time

LEDPIN = 17

def setup():
    global p
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPIN,GPIO.OUT,initial=GPIO.LOW)

    p = GPIO.PWM(LEDPIN, 100)
    p.start(0)

def main():
    internal = 0.01
    while True:
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            time.sleep(internal)
        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(internal)

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

