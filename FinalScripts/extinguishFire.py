import extinguisher
from time import sleep

def extinguishFire():
	extinguisher.start()
	sleep(.5)
	extinguisher.stop()

if __name__ == '__main__':
	extinguishFire()