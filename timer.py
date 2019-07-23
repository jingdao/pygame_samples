import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((810, 200))
font = pygame.font.SysFont("freesansmono", 250)

milliseconds = 0
seconds = 0
minutes = 0
fps = 21
ms_per_frame = 1000.0 / fps
running = False

def update_screen():
	screen.fill((255,255,255))
	text = font.render("%02d:%02d:%03d"%(minutes, seconds, milliseconds), True, (0,0,0))
	rect = text.get_rect()
	screen.blit(text, rect)
	pygame.display.flip()
update_screen()

#game loop
clock = pygame.time.Clock()
while True:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type==KEYDOWN:
			if event.key == K_SPACE:
				running = not running
			elif event.key == K_r:
				milliseconds = 0
				seconds = 0
				minutes = 0
				running = False
				update_screen()
	if running:
		milliseconds += ms_per_frame
		if milliseconds >= 1000:
			milliseconds -= 1000
			seconds += 1
		if seconds >= 60:
			seconds -= 60
			minutes += 1
		update_screen()

