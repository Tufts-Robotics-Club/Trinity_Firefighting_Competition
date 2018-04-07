import RPi.GPIO as GPIO
lists = [[18,49],[25,36], [8,23], [7, 10], [1, -3.5], [17, -49], [27, -36], [22, -23], [10, -10] , [9, 3.5]]
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
	temp = len(angle)
	if temp == 0:
		temp = 1
	return (sum(angle)/temp)+49