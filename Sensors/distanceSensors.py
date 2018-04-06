import RPi.GPIO as GPIO

ULTRASONICS_PINS = [[1, 2], [3, 4]];

GPIO.setmode(GPIO.BCM)
GPIO.setup(ULTRASONICS_PINS, GPIO.IN)

def getDistances():
	distances = []
	for pin_combination in ULTRASONICS_PINS:
		distances.append(_getDistance(pin_combination))

def _getDistance(pin_combination):
	TRIGGER = pin_combination(1)
	ECHO = pin_combination(2)


if __name__ == '__main__':
	getDistances()

