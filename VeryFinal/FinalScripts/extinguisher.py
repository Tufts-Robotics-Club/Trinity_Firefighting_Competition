import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
a = GPIO.PWM(18, 50)

def start():
	a.start(6)
def stop():
	a.start(2.4)