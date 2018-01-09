from grove.grovepi import *
from time import sleep
import random

def turnon(l):
        #pinmode(l, "OUTPUT")
        digitalWrite(l,1)
        print "Led on"

def turnoff(l):
       # pinmode(l, "OUTPUT")
        digitalWrite(l,0)
        print "Led off"

def changer(l):
	for i in range(3):
       		digitalWrite(l,1)
		sleep(0.1)
		digitalWrite(l,0)
		sleep(0.1)
        sleep(2)
#end


l=4
while True:
	analogWrite(l,10)
	print "led"

#while True:
#        pinMode(l, "OUTPUT")
#        try:
#                turnon(l)
#		sleep(2)
#		changer(l)
#                #print "Led off"
#                turnoff(l)
#                #print "led on"
#        except KeyboardInterrupt:
#                digitalWrite(l,0)
#                break
#        except IOError:
#                print "Erreur"
