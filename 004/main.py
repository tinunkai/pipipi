#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

BuzzerPin = 18

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.HIGH)

def main():
    while True:
        play('1')
        play('2')
        play('3')
        play('4')
        play('5')
        play('6')
        play('7')
        play('8')

def play(note):
    do = 1e1
    rate = 2 ** (1/12)
    total = 0.3

    dic = {
          '1': do,
          '2': do * pow(rate, 2),
          '3': do * pow(rate, 4),
          '4': do * pow(rate, 5),
          '5': do * pow(rate, 7),
          '6': do * pow(rate, 9),
          '7': do * pow(rate, 11),
          '8': do * pow(rate, 12)
          }
    internal = total / dic[note]

    per = 0.
    while per < total:
        GPIO.output(BuzzerPin, GPIO.LOW)
        time.sleep(internal)
        GPIO.output(BuzzerPin, GPIO.HIGH)
        time.sleep(internal)
        per += internal
      

def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()    

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()

