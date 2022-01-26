import RPi.GPIO as GPIO
import time
trigger_pin = 23
echo_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def send_trigger_pulse():
	GPIO.output(trigger_pin, True)
	time.sleep(0.001)
	GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):#計算回應時間
	count = timeout
	while GPIO.input(echo_pin) != value and count > 0:
		count = count - 1

def get_distance():
	send_trigger_pulse()#測試23(trigger_pin)是否正常工作
	wait_for_echo(True, 5000)
	start = time.time()
	wait_for_echo(False, 5000)
	finish = time.time()
	pulse_len = finish - start
	distance_cm = pulse_len * 340 *100 /2
	distance_in = distance_cm / 2.5
	print("cm=%f\tinches=%f" % get_distance())#顯示距離
	time.sleep(1)
	return (distance_cm)
