#--------imports and inits
import pygame
import serial
from pygame.locals import *
pygame.init()
pygame.font.init()
#ser=serial.Serial("/dev/ttyACM0", 9600)


#-------functions and constanst
SCWIDTH=500
SCHEIGHT=600
SCR=pygame.display.set_mode((SCWIDTH, SCHEIGHT))
pygame.display.set_caption("Tank drive")
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
leftTread=[False, False]
rightTread=[False, False]
pygame.draw.rect(SCR, (BLUE), (0, 100, 100, 100), 0)




#-------main

done=False
tick=pygame.time.Clock()
while done!=True:
	tick.tick(60)
	#Key checker for movement
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key==K_KP7:
				if leftTread[1]==True:
					print("Motor error")
				else:
					leftTread[0]=True
					#ser.write("LM forward")
			if event.key==K_KP4:
				if leftTread[0]==True:
					print("Motor error")
				else:
					leftTread[1]=True
					#ser.write("LM backward")
			if event.key==K_KP9:
				if rightTread[1]==True:
					print("Motor error")
				else:
					rightTread[0]=True
					#ser.write("RM forward")
			if event.key==K_KP6:
				if rightTread[0]==True:
					print("Motor error")
				else:
					rightTread[1]=True
					#ser.write("LM backward")
		if event.type == pygame.KEYUP:
			if event.key==K_KP7:
				leftTread[0]=False
				#ser.write("lmf off")
			if event.key==K_KP4:
				leftTread[1]=False
				#ser.write("lmb off")
			if event.key==K_KP9:
				rightTread[0]=False
				#ser.write("rmf off")
			if event.key==K_KP6:
				rightTread[1]=False
				#ser.write("rmb off")
	#registering the movement
	
	if leftTread[0]:
		pygame.draw.rect(SCR, (BLUE), (0, 100, 100, 100), 0)
	else:
		pygame.draw.rect(SCR, (RED), (0, 100, 100, 100), 0)
	if leftTread[1]:
		pygame.draw.rect(SCR, (BLUE), (0, 350, 100, 100), 0)
	else:
		pygame.draw.rect(SCR, (RED), (0, 350, 100, 100), 0)
	if rightTread[0]:
		pygame.draw.rect(SCR, (BLUE), (400, 100, 100, 100), 0)
	else:
		pygame.draw.rect(SCR, (RED), (400, 100, 100, 100), 0)
	if rightTread[1]:
		pygame.draw.rect(SCR, (BLUE), (400, 350, 100, 100), 0)
	else:
		pygame.draw.rect(SCR, (RED), (400, 350, 100, 100), 0)
	
	
	pygame.display.update()
