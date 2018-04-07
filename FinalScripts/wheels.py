import move

motor1 = move.servoMove(14)
motor2 = move.servoMove(15)

def moveWheels(left, right):
	motor1.move(left)
	motor2.move(-right)

def rotate(speed):
	moveWheels(speed, speed)