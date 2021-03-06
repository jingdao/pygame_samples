import random
from tetris_helper import *

#variables that store the state of the game
game_over = False
current_tile = None
board_state = [[False for i in range(tiles_horizontal)] for j in range(tiles_vertical)]

#initialize game window
screen = pygame.display.set_mode((tiles_horizontal*tile_size,tiles_vertical*tile_size))

#game loop
clock = pygame.time.Clock()
ticks = 0
while True:
	clock.tick(30)
	if ticks % 30 == 0 and not game_over:
		if current_tile is None:
			current_tile = Tile(random.randint(0,6))
			current_tile.draw(screen)
			if current_tile.is_intersecting(board_state):
				game_over = True
		else:
			current_tile.erase(screen)
			current_tile.move_down(board_state)
			current_tile.draw(screen)
			if current_tile.is_stuck(board_state):
				board_state = clear_rows(screen,board_state)
				current_tile = None
	ticks += 1
	for event in pygame.event.get():
		if event.type == KEYDOWN and current_tile is not None and not game_over:
			if event.key == K_UP:
				print('UP button pressed')
				current_tile.erase(screen)
				current_tile.rotate(board_state)
				current_tile.draw(screen)
			elif event.key == K_LEFT:
				print('LEFT button pressed')
				current_tile.erase(screen)
				current_tile.move_left(board_state)
				current_tile.draw(screen)
			elif event.key == K_RIGHT:
				print('RIGHT button pressed')
				current_tile.erase(screen)
				current_tile.move_right(board_state)
				current_tile.draw(screen)
			elif event.key == K_DOWN:
				print('DOWN button pressed')
				current_tile.erase(screen)
				current_tile.move_down(board_state)
				current_tile.draw(screen)
			elif event.key == K_SPACE:
				current_tile.erase(screen)
				current_tile.drop(board_state)
				current_tile.draw(screen)
				if current_tile.is_stuck(board_state):
					board_state = clear_rows(screen,board_state)
					current_tile = None
