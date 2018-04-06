import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)

def any_on():
	return GPIO.input(14) or GPIO.input(15) or GPIO.input(18) or GPIO.input(23) or GPIO.input(24)
