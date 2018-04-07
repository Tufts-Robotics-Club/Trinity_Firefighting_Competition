import RPi.GPIO as GPIO
import time
import numpy as np

#ULTRASONICS_PINS = [[4, 20]]; #TRIGGER then ECHO
ULTRASONICS_PINS = [20,16, 21, 5, 13, 26, 6, 19]; #TRIGGER then ECHO
TIMEOUT = 6/343
TRIG = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for Echo in ULTRASONICS_PINS:
	GPIO.setup(Echo, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)

def getDistances():
	distances = []

	init_time = time.time()
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	pulse_start = [time.time()] * len(ULTRASONICS_PINS)
	pulse_stop = [time.time()] * len(ULTRASONICS_PINS)
	seen_pulse = [False] * len(ULTRASONICS_PINS)
	stopped_pulse = [False] * len(ULTRASONICS_PINS)


	while (time.time() < init_time + TIMEOUT):
		for index, pin_combo in enumerate(ULTRASONICS_PINS):
			if GPIO.input(pin_combo) == 1:
				if not seen_pulse [index]:
					pulse_start[index] = time.time()
					seen_pulse[index] = True
			if seen_pulse[index] and GPIO.input(pin_combo) == 0 and not stopped_pulse[index]:
				pulse_stop[index] = time.time()
				stopped_pulse[index] = True;
	distances = []

	for index, val in enumerate(pulse_stop):
		distances.append((val - pulse_start[index]) * 17150)

	return distances

def getMedianDistances(num):
	lists = []
	a = []
	for i in range(0,num):
		distances = getDistances()
		lists.append(distances)
	lists = np.array(lists)
	lists = lists.transpose()
	for i in lists:
		a.append(np.median(i))
	return a

def isEcho():
	for pin in ULTRASONICS_PINS:
		if GPIO.input(pin[1]) == True:
			return True
	return False


def __del__():
	for PINS in ULTRASONICS_PINS:
		for PIN in PINS:
			GPIO.cleanup(PIN)


if __name__ == '__main__':
	try:
		lists = [] 
		while True:
			dist = getMedianDistances(5)
			print (dist[7])
			print('-----------------------')
	except KeyboardInterrupt:
		__del__()
