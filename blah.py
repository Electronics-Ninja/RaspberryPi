import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

while True:
	GPIO.output(5, True)
	time.sleep(10)
	GPIO.output(5, False)
	time.sleep(2)
