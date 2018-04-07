import RPi.GPIO as GPIO
import extinguisher
from time import sleep

LIGHT_PIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
def extinguishFire():
	extinguisher.start()
	sleep(.5)
	extinguisher.stop()

if __name__ == '__main__':
	GPIO.output(LIGHT_PIN, 1)
	extinguishFire()
	GPIO.output(LIGHT_PIN, 0)