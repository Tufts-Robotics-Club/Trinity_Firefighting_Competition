# Script to move the servo

import RPi.GPIO as GPIO

# function from rom StackOverflow
def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def change(value):
    return translate(value, -100, 100, 6.0, 8.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 50)


while True:
    inp = input("Input the speed")
    inp = float(inp)
    if (inp < -100 or inp > 100):
        break
    if (inp == 0):
        p.stop()
    else:
        p.ChangeFrequency(50)
        speed = change(inp)
        p.start(speed)
p.stop()
GPIO.cleanup()