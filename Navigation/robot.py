import move

motor1 = move.servoMove(23)
motor2 = move.servoMove(24)

def moveWheels(left, right):
	motor1.move(left)
	right = -right
	motor2.move(right)
