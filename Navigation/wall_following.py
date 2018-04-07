import robot
import distanceSensors
import time

TARGET_DISTANCE = 10 #cm

def wall_following_mode():
	while True:
		dist = distanceSensors.getMedianDistances(3)
		front_distance = dist(2)
		right_distance = dist(0)

		front_on = front_distance > TARGET_DISTANCE
		right_on = right_distance < TARGET_DISTANCE

		if (not front_on and not right_on):
			robot.rotate(-50)
		elif (front_on and not right_on):
			robot.rotate(50)
		elif (front_off and right_on):
			robot.moveWheels(50, 50)
		elif (front_on and right_on):
			robot.rotate(50)

		time.sleep(.5)