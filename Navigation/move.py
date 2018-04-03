# Class for moving servo
# yet to be tested

class servoMove:
	import RPi.GPIO as GPIO
	def __init__(self, pin):
	    GPIO.setmode(GPIO.BCM)
	    GPIO.setup(pin, GPIO.OUT)
	    self.pwm = GPIO.PWM(pin, 50)

	def translate(value, leftMin, leftMax, rightMin, rightMax):
	    leftSpan = leftMax - leftMin
	    rightSpan = rightMax - rightMin
	    valueScaled = float(value - leftMin) / float(leftSpan)
	    return rightMin + (valueScaled * rightSpan)

	def change(value):
	    return self.translate(value, -100, 100, 6.0, 8.5)

	def move(inp):
		inp = float(inp)
	    if (inp == 0):
	        self.pwm.stop()
	    else:
	        self.pwm.ChangeFrequency(50)
	        speed = self.change(inp)
	        self.pwm.start(speed)

