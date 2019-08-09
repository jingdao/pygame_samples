import pygame
from pygame.locals import *
import random

tile_size = 50
tiles_horizontal = 20
tiles_vertical = 20

screen = pygame.display.set_mode((tiles_horizontal*tile_size,tiles_vertical*tile_size))

snake_head_img = pygame.image.load('snake_head.png')
snake_body_img = pygame.image.load('snake_body.png')
apple_img = pygame.image.load('apple.png')

apple_x = random.randint(0, tiles_horizontal-1)
apple_y = random.randint(0, tiles_vertical-1)
snake_head_x = tiles_horizontal // 2
snake_head_y = tiles_vertical // 2
snake_body = [
	[snake_head_x - 3, snake_head_y],
	[snake_head_x - 2, snake_head_y],
	[snake_head_x - 1, snake_head_y],
]
snake_direction_x = 1
snake_direction_y = 0
snake_length = 3
apples_consumed = 0

def update_display():
	screen.fill((150,150,150))
	screen.blit(apple_img, (apple_x * tile_size, apple_y * tile_size))
	screen.blit(snake_head_img, (snake_head_x * tile_size, snake_head_y * tile_size))
	for x,y in snake_body:
		screen.blit(snake_body_img, (x * tile_size, y * tile_size))
	pygame.display.flip()
update_display()

#game loop
clock = pygame.time.Clock()
ticks = 0
game_over = False
while True:
	clock.tick(30)
	if game_over:
		continue
	if ticks % 5 == 0:
		snake_body.append([snake_head_x, snake_head_y])
		if len(snake_body) > snake_length:
			del snake_body[0]
		snake_head_x += snake_direction_x
		snake_head_y += snake_direction_y
		if snake_head_x < 0 or snake_head_x >= tiles_horizontal or snake_head_y < 0 or snake_head_y >= tiles_vertical or \
			any([snake_head_x==x and snake_head_y==y for x,y in snake_body]):
			game_over = True
			print('Game Over!')
			continue
		if snake_head_x == apple_x and snake_head_y == apple_y:
			apples_consumed += 1
			print('apples_consumed =',apples_consumed)
			snake_length += 2
			while apple_x==snake_head_x and apple_y==snake_head_y or \
				any([apple_x==x and apple_y==y for x,y in snake_body]):
				apple_x = random.randint(0, tiles_horizontal-1)
				apple_y = random.randint(0, tiles_vertical-1)
		update_display()
	ticks += 1
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_UP:
				snake_direction_x = 0
				snake_direction_y = -1
			elif event.key == K_LEFT:
				snake_direction_x = -1
				snake_direction_y = 0
			elif event.key == K_DOWN:
				snake_direction_x = 0
				snake_direction_y = 1
			elif event.key == K_RIGHT:
				snake_direction_x = 1
				snake_direction_y = 0
