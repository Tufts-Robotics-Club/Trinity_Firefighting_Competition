import serial
from time import sleep
ser = serial.Serial('/dev/ttyACM4')
def getDistances():
	ser.write(b'1')
	read_serial=ser.readline()
	read_serial = read_serial.decode("utf-8")
	read_serial = read_serial.replace("\r\n", "")
	distances = read_serial.split(" ")
	distances = [int(numeric_string) for numeric_string in distances]
	return distances

