import pygame
from pygame.locals import *

#define some constants
tile_size = 30
tiles_horizontal = 10
tiles_vertical = 20
tile_shape = [
	[(0,-1),(0,0),(0,1),(0,2)],
	[(-1,-1),(0,-1),(-1,0),(0,0)],
	[(-1,-1),(0,-1),(0,0),(1,0)],
	[(-1,0),(0,-1),(0,0),(1,-1)],
	[(0,-1),(0,0),(-1,0),(1,0)],
	[(-1,-1),(0,-1),(0,0),(0,1)],
	[(1,-1),(0,-1),(0,0),(0,1)],
]
tile_color = [
	(255,0,0),
	(0,255,0),
	(0,0,255),
	(255,255,0),
	(255,0,255),
	(0,255,255),
	(128,128,128),
]

#class that provides attributes and methods for Tiles
class Tile:
	def __init__(self,type_id):
		self.shape = tile_shape[type_id]
		self.color = tile_color[type_id]
		self.position = [tiles_horizontal//2, 1]

	def erase(self,screen):
		for dx,dy in self.shape:
			x = (self.position[0] + dx) * tile_size
			y = (self.position[1] + dy) * tile_size
			screen.fill((0,0,0),(x,y,tile_size,tile_size))
		pygame.display.flip()
	
	def draw(self,screen):
		for dx,dy in self.shape:
			x = (self.position[0] + dx) * tile_size
			y = (self.position[1] + dy) * tile_size
			screen.fill(self.color,(x,y,tile_size,tile_size))
		pygame.display.flip()

	def rotate(self, board_state):
		rotated_shape = [(y,-x) for x,y in self.shape]
		for dx,dy in rotated_shape:
			if self.position[0] + dx < 0 or self.position[0] + dx > tiles_horizontal - 1 or \
				self.position[1] + dy < 0 or self.position[1] + dy > tiles_vertical - 1:
					return #rotated shape goes out of bounds
		if any(map(lambda x:board_state[x[1]+self.position[1]][x[0]+self.position[0]], rotated_shape)):
			return #rotated shape intersects other tiles
		self.shape = rotated_shape
	
	def move_down(self, board_state):
		self.position[1] += 1
		if self.is_intersecting(board_state):
			self.position[1] -= 1

	def move_left(self, board_state):
		if all(map(lambda x:x[0]+self.position[0] > 0, self.shape)):
			self.position[0] -= 1
			if self.is_intersecting(board_state):
				self.position[0] += 1
		
	def move_right(self, board_state):
		if all(map(lambda x:x[0]+self.position[0] < tiles_horizontal - 1, self.shape)):
			self.position[0] += 1
			if self.is_intersecting(board_state):
				self.position[0] -= 1

	def is_stuck(self,board_state):
		if any(map(lambda x:x[1]+self.position[1] == tiles_vertical-1, self.shape)) \
			or any(map(lambda x:board_state[x[1]+self.position[1]+1][x[0]+self.position[0]], self.shape)): 
			for dx,dy in self.shape:
				board_state[self.position[1] + dy][self.position[0] + dx] = True
			return True
		return False
	
	def is_intersecting(self,board_state):
		return any(map(lambda x:board_state[x[1]+self.position[1]][x[0]+self.position[0]], self.shape))

	def drop(self,board_state):
		while not self.is_stuck(board_state):
			self.move_down(board_state)

#clear rows that are filled
def clear_rows(screen,board_state):
	rows_cleared = sum([all(b) for b in board_state])
	if rows_cleared == 0:
		return board_state
	rows_remaining = tiles_vertical - rows_cleared
	new_state = [[False for k in range(tiles_horizontal)] for l in range(rows_cleared)]
	cropped = pygame.Surface((tiles_horizontal*tile_size,rows_remaining*tile_size))
	j = 0
	for i in range(tiles_vertical):
		if not all(board_state[i]):
			new_state.append(board_state[i])
			cropped.blit(screen,(0,j*tile_size),(0,i*tile_size,tiles_horizontal*tile_size,tile_size))
			j += 1
	screen.fill((0,0,0),(0,0,tiles_horizontal*tile_size,rows_cleared*tile_size))
	screen.blit(cropped,(0,rows_cleared*tile_size))
	pygame.display.flip()
	return new_state
	
