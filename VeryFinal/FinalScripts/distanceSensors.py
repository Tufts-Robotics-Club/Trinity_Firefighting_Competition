import numpy as np
import serial

ser = serial.Serial('/dev/ttyACM0')

def getDistances():
        ser.write(b'1')
        read_serial=ser.readline()
        read_serial = read_serial.decode("utf-8")
        read_serial = read_serial.replace("\r\n", "")
        distances = read_serial.split(" ")
        distances = [int(numeric_string) for numeric_string in distances]
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

if __name__ == "__main__":
	while True:
		print(getMedianDistances(3))
