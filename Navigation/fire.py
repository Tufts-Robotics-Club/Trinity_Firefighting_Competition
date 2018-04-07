import RPi.GPIO as GPIO
lists = [[18,10],[25,30], [8,50], [7, 70], [1, 90]]
GPIO.setmode(GPIO.BCM)

for pins in lists:
	GPIO.setup(pins[0], GPIO.IN)

def any_on():
	for pins in lists:
		if GPIO.input(pins[0]):
			return True
	return False

def angle():
	angle = []
	for pins in lists:
		if GPIO.input(pins[0]):
			angle.append(pins[1])
	return sum(angle)/len(angle)
