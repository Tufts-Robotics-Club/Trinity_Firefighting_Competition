import RPi.GPIO as GPIO
import time

#ULTRASONICS_PINS = [[4, 20]]; #TRIGGER then ECHO
ULTRASONICS_PINS = [[4, 20], [4, 16], [4, 21], [4, 5],
 						[4, 6], [4, 13], [4, 19], [4, 19]]; #TRIGGER then ECHO
TIMEOUT = 6/343

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for PINS in ULTRASONICS_PINS:
	GPIO.setup(PINS[0], GPIO.OUT)
	GPIO.setup(PINS[1], GPIO.IN)

def getDistances():
	distances = []

	while isEcho():               #Check whether the ECHO is LOW
		pulse_start = time.time() #Saves the last known time of LOW pulse

	GPIO.output(TRIG, True)                  #Set TRIG as HIGH
	time.sleep(0.00001)                      #Delay of 0.00001 seconds
	GPIO.output(TRIG, False)                 #Set TRIG as LOW
	
	pulse_stop = [pulse_start] * len(ULTRASONICS_PINS)
	seen_pulse = [False] * len(ULTRASONICS_PINS)

	while not (all(seen_pulse) and not isEcho()) or (time.time() < pulse_start+TIMEOUT):
		for index, pin_combo in enumerate(ULTRASONICS_PINS):
			if GPIO.input(pin_combo[1]) == 1
				pulse_stop[index] = time.time()
				seen_pulse[index] = True

    distances = []

    for index, val in enumerate(pulse_stop):
    	distances[index] = (pulse_stop[index] - pulse_start) * 17150

	return distances

def isEcho():
	for pin in ULTRASONICS_PINS:
		if GPIO.input(pin[1]) == True:
			return True
	return False

def _getDistance(pin_combination):
	TRIG = pin_combination[0]
	ECHO = pin_combination[1]

	GPIO.output(TRIG, False)                 #Set TRIG as LOW
	print "Waitng For Sensor To Settle"
	time.sleep(2)                            #Delay of 2 seconds



	while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
		pulse_start = time.time()              #Saves the last known time of LOW pulse

	while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
		pulse_end = time.time()                #Saves the last known time of HIGH pulse 

	pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

	distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
	distance = round(distance, 2)            #Round to two decimal points

	if True:      #Check whether the distance is within range
		print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
	else:
		print"Out Of Range"                   #display out of range

	return distance

def __del__():
	for PINS in ULTRASONICS_PINS:
		for PIN in PINS:
			GPIO.cleanup(PIN)



if __name__ == '__main__':
	try:
		while True:
			getDistances()
			time.sleep(1)
			print('-----------------------')
	except KeyboardInterrupt:
		__del__()