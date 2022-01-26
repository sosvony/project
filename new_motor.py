import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Fre = 400
stepPin[4] = [11,13,15,19]
dirPin[4] = [12,16,18,22]

for i in range(4):
	GPIO.setup(stepPin[i], GPIO.OUT)
	GPIO.setup(dirPin[i], GPIO.OUT)

def wheel(w1, w2, w3, w4)
	GPIO.output(stepPin[1], w1)
	GPIO.output(stepPin[2], w2)
	GPIO.output(stepPin[3], w3)
	GPIO.output(stepPin[4], w4)

def stop()
	wheel(0, 0, 0, 0)

def forwork():
	wheel(1, 1, 1, 1)

