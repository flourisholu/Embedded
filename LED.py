import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) #set header strip to be layed out as it is on the Pi

blinkCount = 3 #cycle through switching on and off before safely close
count = 0
LEDPin = 22
buttonPin = 5

#Set up the pin that the LED is connected to
GPIO.setup(LEDPin, GPIO.OUT)
#Set up the button
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) #button is currently in up position

buttonPress = True #keep track of state of button
ledState = False #keep track of state of LED

try:
	while count < blinkCount:
		print ("Press that button")
		buttonPress = GPIO.input(buttonPin)
		if buttonPress == False and ledState == False:
			GPIO.output(LEDPin, True)
			print("LED ON")
			ledState = True
			sleep(3)
		elif buttonPress == False and ledState == True:
			GPIO.output(LEDPin, False)
			print("LED OFF")
			ledState = False
			count = count + 1
			sleep(0.5)
		sleep(0.1) #add a break to keep pi safe
finally:
	#Reset the GPIO pins to a safe state and clear up all resources
	GPIO.cleanup()
