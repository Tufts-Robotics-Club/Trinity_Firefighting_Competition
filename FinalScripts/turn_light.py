import Rpi.GPIO as GPIO
import time

LIGHT_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

def light_pin_up_for(pin, t):
	GPIO.output(LIGHT_PIN, True)
	time.sleep(t)
	GPIO.output(LIGHT_PIN, False)