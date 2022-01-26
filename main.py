from cam import camera
from echo import get_distance
from motor import turnLeft, turnRight, forward
from time import sleep

while True:
	# QR code 資料
	coor_x, coor_y, Data = camera()
	# 距離
	dir = get_distance()
	# 顯示ＱＲ code 資料
	print("[INFO] 1. ",Data)
	# 顯示距離
	print("[INFO] 2. " ,dir ," cm")

	if coor_x != 0 & coor_y != 0:
		# 方向控制 (左)
		if coor_x < 150 :
			turnLeft()
			print("[INFO] 3. Turn Left")

		# 方向控制 (右)	
		elif coor_x > 150:
			turnRight()
			print("[INFO] 3. Turn Right")

		# 方向控制 
		else:
			if dir > 20:
				forward()
			else:
				turnLeft()