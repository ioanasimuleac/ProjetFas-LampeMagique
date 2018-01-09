#!/usr/bin/env python

import time
import grove.grovepi

# Connect the Grove Light Sensor to analog port A0
light_sensor = 0

# Connect the LED to digital port D4
led = 4

# Turn on LED once sensor exceeds threshold resistance
threshold = 10

grove.grovepi.pinMode(light_sensor,"INPUT")
grove.grovepi.pinMode(led,"OUTPUT")
sensor_value = grove.grovepi.analogRead(light_sensor)
print("sensor " + str(sensor_value))
resistance = (float)(1023 - sensor_value) * 10 / sensor_value
