import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
a = GPIO.PWM(2, 50)

def woosh():
	a.start(5)
def close():
	a.start(2.5)