import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.LOW)

LED_ON = 1
LED_OFF = 0
state = LED_OFF
input_user = LED_OFF

while True:
	input_user = int(input("Digite: 1 para ligar led, 0 para desligar led: "))
	if (state == LED_OFF):
		if (input_user == LED_ON):
			GPIO.output(12, GPIO.HIGH)
			state=LED_ON
	elif (state == LED_ON):
		if(input_user == LED_OFF):
			GPIO.output(12, GPIO.LOW)
			state=LED_OFF
