from wheels import rotate, moveWheels
from time import sleep

def traverseMaze():
	moveWheels(100, 100)
	sleep(3)
	moveWheels(0, 0)

if __name__ == '__main__':
	traverseMaze()
