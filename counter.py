#! /usr/bin/python

######################################################
# Simple Counter Program                             # 
#                                                    #
# Used with a Raspberry Pi B+                        #
#  (can be used with other RPi's, just need to       #
#    adjust the pins used)                           #
# and 2 4026 decade counters                         #
# and 1 3 7-segment display (only 2 are used)        #
# Also need a tactile switch                         #
# and a couple LEDs, a few resistors and a capacitor #
#                                                    #
# https://github.com/Electronics-Ninja/RaspberryPi   #
#                                                    #
######################################################

__author__    = "Paul Kincaid" 
__copyright__ = "Copyright 2015"
__license__   = "GPL"
__version__   = "1.0"
__email__     = "paul.m.kincaid@gmail.com"


import RPi.GPIO as GPIO
import time, os, sys

GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

used_pins = (5, 16)

for reset in used_pins:
        GPIO.output(reset, False)

GPIO.setup(20, GPIO.IN)
i = 0
while True:
        try:
                if GPIO.input(20) and i == 0:
                        GPIO.output(5, True)
                        time.sleep(1)
                        GPIO.output(5, False)
                        time.sleep(1)
                        i = 1
                elif i == 1:
                        GPIO.output(5, True)
                        time.sleep(1)
                        GPIO.output(5, False)
                        time.sleep(1)
                if GPIO.input(20) and i == 1:
                        i = 0
                        time.sleep(1)

        except(KeyboardInterrupt):
                GPIO.output(16, True)
                GPIO.output(16, False)
                GPIO.cleanup()
                raise

GPIO.cleanup()
