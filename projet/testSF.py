#!/usr/bin/env python

import time
import grove.grovepi
from light.Fonclight import *
# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

grove.grovepi.pinMode(light_sensor,"INPUT")
grove.grovepi.pinMode(led,"OUTPUT")
f = open("light.txt", 'w')
while True:
	try:
       		# Get sensor value
        	sensor_value = analogRead(light_sensor)
        	print("sensor " + str(sensor_value))

        	# Calculate resistance of sensor in K
        	resistance = (float)(1023 - sensor_value) * 10 / sensor_value
		print("res " + str(resistance))
		f.write(str(sensor_value))
		f.write("\n")

        	if sensor_value < 200:
            		# Send HIGH to switch on LED
            		grove.grovepi.digitalWrite(led,1)
            	else:	# Send LOW to switch off LED
            		grove.grovepi.digitalWrite(led,0)
	       # print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance$)
		time.sleep(2)
	except KeyboardInterrupt:
		break
	except IOError:
		print "erreur"


f.close()

