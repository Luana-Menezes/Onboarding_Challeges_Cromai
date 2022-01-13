from time import sleep, time
from picamera import PiCamera
from datetime import datetime
import os
import csv

def get_datetime_now():
	datetime_today = datetime.now()
	str_date_today = datetime_today.strftime('%b %d, %Y')

	str_time_today = datetime_today.strftime('%H:%M:%S')
	print(str_date_today + ' ' + str_time_today)
	return [str_date_today, str_time_today]

def capture_photo():
	camera = PiCamera()
	camera.resolution = (1662, 1232)
	camera.rotation = -90
	#camera.exposure_mode = 'fireworks'
	#camera.awb_mode = 'flash'
	#dormir
	sleep(2)
	filename = 'image_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.jpg'	
	camera.capture('./photos/' + filename)	
	fullpath = os.getcwd() + '/photos/' + filename	
	print("Foto Capturada: " + fullpath)
	camera.close()	
	return fullpath

def header_to_csv():
	with open('teste.csv', 'w') as csv_file:
                writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
                writer.writerow(['image_path','date','time'])
		
def append_to_csv():
	with open('teste.csv', 'a') as csv_file:
		writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		photo = capture_photo()
		date, time = get_datetime_now() 
		writer.writerow([photo,date,time])
		
with open('teste.csv','r') as file:
	reader = csv.reader(file)
	lines = len(list(reader))

if lines == 1:
	header_to_csv()

while True:
	append_to_csv()
	sleep(1)
