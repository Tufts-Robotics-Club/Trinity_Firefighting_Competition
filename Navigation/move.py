# Class for moving servo
# yet to be tested

class servoMove:
	def __init__(self, pin):
		import RPi.GPIO as GPIO
	    GPIO.setmode(GPIO.BCM)
	    GPIO.setup(pin, GPIO.OUT)
	    self.pwm = GPIO.PWM(pin, 50)
	    self.speed = 0
	    self.pin = pin

	def translate(value, leftMin, leftMax, rightMin, rightMax):
	    leftSpan = leftMax - leftMin
	    rightSpan = rightMax - rightMin
	    valueScaled = float(value - leftMin) / float(leftSpan)
	    return rightMin + (valueScaled * rightSpan)

	def change(self, value):
	    return self.translate(value, -100, 100, 6.0, 8.5)

	def move(self, inp):
		inp = float(inp)
		self.speed = inp
	    if (inp == 0):
	        self.pwm.stop()
	    else:
	        self.pwm.ChangeFrequency(50)
	        speed = self.change(inp)
	        self.pwm.start(speed)

	def __del__(self):
		p.stop(self.pin)
    	GPIO.cleanup(self.pin)