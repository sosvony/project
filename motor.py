import RPi.GPIO as GPIO
import time

step1_Pin=9
step2_Pin=11
step3_Pin=19
step4_Pin=26
dir1_Pin=25
dir2_Pin=8
dir3_Pin=16
dir4_Pin=20
sleep_time=1
fre=200
GPIO.setup(9, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

# times = fre * sleep = 200ms * 1 = 2s

def forward():
	for i in range(fre):
		GPIO.output(step1_Pin,True)
		GPIO.output(step2_Pin,True)
		GPIO.output(step3_Pin,True)      
		GPIO.output(step4_Pin,True)
		time.sleep(sleep_time)
		GPIO.output(step1_Pin,False)
		GPIO.output(step2_Pin,False)
		GPIO.output(step3_Pin,False)
		GPIO.output(step4_Pin,False)
	GPIO.output(dir1_pin, False)
	GPIO.output(dir2_pin, True)
	GPIO.output(dir3_pin, False)
	GPIO.output(dir4_pin, True)
def back():
	for i in range(fre):
		GPIO.output(step1_Pin,True)
		GPIO.output(step2_Pin,True)
		GPIO.output(step3_Pin,True)      
		GPIO.output(step4_Pin,True)
		time.sleep(sleep_time)
		GPIO.output(step1_Pin,False)
		GPIO.output(step2_Pin,False)
		GPIO.output(step3_Pin,False)
		GPIO.output(step4_Pin,False)
	GPIO.output(dir1_pin, True)
	GPIO.output(dir2_pin, False)
	GPIO.output(dir3_pin, True)
	GPIO.output(dir4_pin, False)
def turnLeft():
	for i in range(fre):
		GPIO.output(step1_Pin,True)
		GPIO.output(step2_Pin,True)
		GPIO.output(step3_Pin,True)      
		GPIO.output(step4_Pin,True)
		time.sleep(sleep_time)
		GPIO.output(step1_Pin,False)
		GPIO.output(step2_Pin,False)
		GPIO.output(step3_Pin,False)
		GPIO.output(step4_Pin,False)
	GPIO.output(dir1_pin, True)
	GPIO.output(dir2_pin, True)
	GPIO.output(dir3_pin, True)
	GPIO.output(dir4_pin, True)
def turnRight():
	for i in range(fre):
		GPIO.output(step1_Pin,True)
		GPIO.output(step2_Pin,True)
		GPIO.output(step3_Pin,True)      
		GPIO.output(step4_Pin,True)
		time.sleep(sleep_time)
		GPIO.output(step1_Pin,False)
		GPIO.output(step2_Pin,False)
		GPIO.output(step3_Pin,False)
		GPIO.output(step4_Pin,False)
	GPIO.output(dir1_pin, False)
	GPIO.output(dir2_pin, False)
	GPIO.output(dir3_pin, False)
	GPIO.output(dir4_pin, False)