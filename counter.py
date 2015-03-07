#! /usr/bin/python

######################################################
# Simple Counter Program                             # 
#                                                    #
# Used with a Raspberry Pi B+                        #
#  (can be used with other RPi's, just need to       #
#    adjust the pins used)                           #
#                                                    #
# https://github.com/Electronics-Ninja/RaspberryPi   #
#                                                    #
# See the Eagle Schematic file for external circuit  #
# Parts List:                                        #
#    - (2) 4026 decade counters                      #
#    - (2) 7-segment displays (common cathode)       #
#    - (1) Tactile switch - SPDT                     #
#    - (3) 1k 1/8-watt resistors                     #
#    - (3) 15k 1/8-watt resistors                    #
#    - (2) 330 ohm 1/8-watt resistors                #
#    - (1) 100uF Electrolytic Capacitor              #
#    - (1) Raspberry Pi B+ (or other model)          #
######################################################

__author__    = "Paul Kincaid" 
__copyright__ = "Copyright 2015"
__license__   = "GPL"
__version__   = "1.0"
__email__     = "paul.m.kincaid@gmail.com"


import RPi.GPIO as GPIO
import time, os, sys

#################################
# Change these to any GPIO pins #
#################################
reset_pin = 16
clock_pin = 5
####### END CHANGE SECTION ######

GPIO.setmode(GPIO.BCM)

GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)

cp = clock_pin
rp = reset_pin

used_pins = (cp, rp)

for reset in used_pins:
        GPIO.output(reset, False)

GPIO.setup(20, GPIO.IN)
i = 0
while True:
        try:
                if GPIO.input(20) and i == 0:
                        GPIO.output(cp, True)
                        time.sleep(1)
                        GPIO.output(cp, False)
                        time.sleep(1)
                        i = 1
                elif i == 1:
                        GPIO.output(cp, True)
                        time.sleep(1)
                        GPIO.output(cp, False)
                        time.sleep(1)
                if GPIO.input(20) and i == 1:
                        i = 0
                        time.sleep(1)

        except(KeyboardInterrupt):
                GPIO.output(rp, True)
                GPIO.output(rp, False)
                GPIO.cleanup()
                raise

GPIO.cleanup()
