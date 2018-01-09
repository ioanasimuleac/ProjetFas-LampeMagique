#from grove.grovepi import *
from time import sleep
from LED.FoncLED import *
from buzzer.Foncbuzzer import *
from light.Fonclight import *
from move.FoncMove import *
import random
import pygame



pygame.mixer.init()
pygame.mixer.music.load("song.mp3")


#les Leds sont trouves a D4, D3, D2
#buzzer sur D7
#motion sensor sur D8
#light sensor sur A1
led1 = 4
led2 = 3
led3 = 2 
leds = [led1,led2, led3]
buzzer = 7
pir = 8
light = 1


variable = 200
f = open ("light.txt", 'w')
#m = open ("move.txt", 'w')
#m = []
mlist = []
turnon=False
while True:
        i = random.randint(0,2)
        l = leds[i]
        try:
		sensor = startLight(light)
		f.write(str(sensor))
		f.close()
		with open("light.txt", 'r') as files:
			ligne = files.readlines()
			print("lignes " + str(ligne))
			if (int(ligne[0]) < variable):
				turnon(l)
				print ("led est: " + str(l))
				move = startMove(pir)
				if move ==1:
					print "motion"
					#commencer la musique
					if not(turnon):
						pygame.mixer.music.play(0)
						pygame.mixer.music.set_volume(1.0)
						turnon=True
				else:
					print "pas de motion"
					turnon=False
					pygame.mixer.music.stop()
					#arreter la musique, mais quand? une liste pour sauvegarder les donnees et les comparer
				mlist = []
				m = open ("move.txt", 'r')
				mlist = m.readlines()
				m.close()

				#with open("move.txt", 'r') as mo:
				#	for line in mo:
				#		mlist.append(int(line.strip()))

				mlist.append(str(move))
				print "salut"
				print mlist
				m = open ("move.txt", 'w')

				for i in mlist:
					m.write(i)
				m.close()

				#with open ("move.txt", 'w') as mo:
				#	for m in mlist:
				#		mo.write(str(m) + "\n")

				#with open("move.txt", 'r') as mo:
				#	mliste = mo.readlines()
				#mliste.append(move)
				#with open("move.txt", 'w') as file_handler:
    				#	file_handler.write(str(mliste))
				#with open("move.txt", 'a+') as m:
				#	m.write(str(move))
				#m.write(str(move))
				#m.close()
			else:
				print "pas led"
				turnoff(l)
				
			
			sleep(3)
			turnoff(l)
			f = open("light.txt", 'w')
			#m = open("move.txt", 'a')
		#f.close()
        except KeyboardInterrupt:
		turnoff(l)
		turnon(buzzer)
		print "buzzer on"
		sleep(0.5)
		turnoff(buzzer)
		print "buzzer off"
		break
        except IOError:
                print "Erreur"

