import RPi.GPIO as GPIO
lists = [[5,-52.5],[6,-38.5], [13,-24.5], [19, -10.5], [26, 3.5], [16, -3.5], [9, 10.5], [10, 24.5], [22, 38.5] , [27, 52.5]]
GPIO.setmode(GPIO.BCM)

for pins in lists:
	GPIO.setup(pins[0], GPIO.IN)

def any_on():
	for pins in lists:
		if GPIO.input(pins[0]):
			return True
	return False
def test():
	for pins in lists:
		print (GPIO.input(pins[0]))
		
def angle():
	angle = []
	for pins in lists:
		if GPIO.input(pins[0]):
			angle.append(pins[1])
	temp = len(angle)
	if temp == 0:
		temp = 1
	return (sum(angle)/temp)