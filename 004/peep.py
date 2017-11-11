#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

BuzzerPin = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.HIGH)

def main():
    total = .02
    do = 1e2
    for _ in range(1, 30):
        do *= 1.1
        internal = total / do
        for _ in range(int(do)):
            GPIO.output(BuzzerPin, GPIO.LOW)
            time.sleep(internal)
            GPIO.output(BuzzerPin, GPIO.HIGH)
            time.sleep(internal)
      

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()    

if __name__ == '__main__':
    setup()
    try:
        while True:
            main()
    except KeyboardInterrupt:
        destroy()

