import pygame
from pygame.locals import *
import random

screen_size = 600
grids = 30
grid_size = int(screen_size / grids)
line_width = 5

screen = pygame.display.set_mode((screen_size, screen_size))

cycle1 = pygame.image.load('yellow.png')
cycle_width = cycle1.get_size()[0]
cycle_height = cycle1.get_size()[1]
screen.blit(cycle1, (grid_size-cycle_width/2, grid_size-cycle_height/2))
cycle2 = pygame.image.load('blue.png')
screen.blit(cycle2, ((grids-1)*grid_size-cycle_width/2, (grids-1)*grid_size-cycle_height/2))

for i in range(1, grids):
	pygame.draw.line(screen, (255,255,255), (i*grid_size, grid_size), (i*grid_size, (grids-1)*grid_size), 1)
	pygame.draw.line(screen, (255,255,255), (grid_size, i*grid_size), ((grids-1)*grid_size, i*grid_size), 1)

pygame.display.flip()

game_start = False
game_over = False
occupied = set()
offset = { 'up': (0,-1), 'down': (0,1), 'left': (-1,0), 'right': (1,0) }
directions = list(offset.keys())
cycle1_pos = (1,1)
cycle1_dir = 'right'
cycle2_pos = (grids-1,grids-1)
cycle2_dir = 'left'

def valid_pos(pos):
	return pos not in occupied and pos[0] > 0 and pos[0] < grids and pos[1] > 0 and pos[1] < grids

def get_ai_move():
	#swerve if obstacle ahead or at random intervals
	next_pos = (cycle2_pos[0] + offset[cycle2_dir][0], cycle2_pos[1] + offset[cycle2_dir][1])
	if not valid_pos(next_pos) or random.randint(1,5)==5:
		random.shuffle(directions)
		for next_dir in directions:
			next_pos = (cycle2_pos[0] + offset[next_dir][0], cycle2_pos[1] + offset[next_dir][1])
			if valid_pos(next_pos):
				return next_dir
		return cycle2_dir
	return cycle2_dir	

clock = pygame.time.Clock()
ticks = 0
while True:
	clock.tick(30)
	if game_start and not game_over and ticks % 10 == 0:
		if not valid_pos(cycle1_pos):
			game_over = True
			print('Game over: blue wins')
		elif not valid_pos(cycle2_pos):
			game_over = True
			print('Game over: yellow wins')
		else:
			new_pos = (cycle1_pos[0] + offset[cycle1_dir][0], cycle1_pos[1] + offset[cycle1_dir][1])
			pygame.draw.line(screen, (255,255,0), (cycle1_pos[0]*grid_size, cycle1_pos[1]*grid_size), (new_pos[0]*grid_size, new_pos[1]*grid_size), line_width)
			occupied.add(cycle1_pos)
			cycle1_pos = new_pos
			cycle2_dir = get_ai_move()
			new_pos = (cycle2_pos[0] + offset[cycle2_dir][0], cycle2_pos[1] + offset[cycle2_dir][1])
			pygame.draw.line(screen, (0,0,255), (cycle2_pos[0]*grid_size, cycle2_pos[1]*grid_size), (new_pos[0]*grid_size, new_pos[1]*grid_size), line_width)
			occupied.add(cycle2_pos)
			cycle2_pos = new_pos
			pygame.display.flip()
	ticks += 1
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_UP:
				cycle1_dir = 'up'
			if event.key == K_DOWN:
				cycle1_dir = 'down'
			if event.key == K_LEFT:
				cycle1_dir = 'left'
			if event.key == K_RIGHT:
				cycle1_dir = 'right'
			game_start = True

