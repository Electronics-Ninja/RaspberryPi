#! /usr/bin/python

######################################################
# Simple BCD 7-segment Driver                        # 
#                                                    #
# Used with a Raspberry Pi B+                        #
#  (can be used with other RPi's, just need to       #
#    adjust the pins used)                           #
#                                                    #
# https://github.com/Electronics-Ninja/RaspberryPi   #
#                                                    #
# See the Eagle Schematic file for external circuit  #
# Parts List:                                        #
#    - (2) 7447 BCD 7-segment driver                 #
#    - (1) 7-segment displays (common anode)         #
#    - (4) 1k 1/4-watt resistors                     #
#    - (1) 470 ohm 1/4-watt                          #
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

a_pin = 17
b_pin = 27
c_pin = 22
d_pin = 13
reset_pin = 16
clock_pin = 5
switch_pin = 20
####### END CHANGE SECTION ######

GPIO.setmode(GPIO.BCM)

GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(reset_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(d_pin, GPIO.OUT)

a = a_pin
b = b_pin
c = c_pin
d = d_pin
cp = clock_pin
rp = reset_pin
sp = switch_pin

used_pins = (cp, rp)

for reset in used_pins:
        GPIO.output(reset, False)
for reset in (a,b,c,d):
	GPIO.output(reset, False)

###### Binary Counting ######
bcd_values = [[], [a], [b], [a,b], [c], [a,c], [b,c], [a,b,c], [d], [a,d]]

i = 0
button_count = bc = 0
num = 0
while True:
	try:
		if GPIO.input(sp):
			if bc == 9:
				bc = -1
			bc = bc + 1
			print bc
			for reset in (a,b,c,d):
				GPIO.output(reset, False)
			for segment in bcd_values[bc]:
				GPIO.output(segment, True)
			time.sleep(0.5)
			num = 0
		if bc % 2 == 1:
			if num == 0:
				print "# should be ODD, start counting"
				num = 1
			GPIO.output(cp, True)
		elif bc % 2 == 0:
			if num == 0:
				print "# should be EVEN, stop counting"
				num = 1
			GPIO.output(cp, False)


#        try:
#                if GPIO.input(sp) and i == 0:
#                        GPIO.output(cp, True)
#                        time.sleep(1)
#                        GPIO.output(cp, False)
#                        time.sleep(1)
#                        i = 1
#			bc = 1
#			GPIO.output(bcd_values[bc], True)
#                elif i == 1:
#                        GPIO.output(cp, True)
#                        time.sleep(1)
#                        GPIO.output(cp, False)
#                        time.sleep(1)
#                if GPIO.input(sp) and i == 1:
#                        i = 0
#			bc = bc + 1
#			for reset in (a,b,c,d):
#				GPIO.output(reset, False)
#			for v in bcd_values[bc]:
#				GPIO.output(v, True)
#                        time.sleep(1)

        except(KeyboardInterrupt):
                GPIO.output(rp, True)
                GPIO.output(rp, False)
                GPIO.cleanup()
                raise

GPIO.cleanup()
