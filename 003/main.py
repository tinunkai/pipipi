#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

ButtonPin = 17
LedPin = 18

led_status = True

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(ButtonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(ButtonPin,GPIO.FALLING,callback = ButtonLed)

def ButtonLed(ev=None):
    global led_status
    led_status = not led_status
    GPIO.output(LedPin, led_status)

def main():
    while True:
        time.sleep(100)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()

