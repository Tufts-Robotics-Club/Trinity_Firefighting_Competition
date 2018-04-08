import RPi.GPIO as GPIO
import time

LIGHT_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

def light_pin_up_for(pin, t):
	GPIO.output(LIGHT_PIN, True)
	time.sleep(t)
	GPIO.output(LIGHT_PIN, False)

if __name__ == '__main__':
	light_pin_up_for(LIGHT_PIN, 1)