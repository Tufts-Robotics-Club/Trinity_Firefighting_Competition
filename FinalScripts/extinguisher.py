import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
a = GPIO.PWM(2, 50)

def start():
	a.start(5)
def stop():
	a.start(2.5)