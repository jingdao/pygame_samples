import pygame
from pygame.locals import *

#initialize game window
screen = pygame.display.set_mode((600,600))

#import image resources
board = pygame.image.load('board.png')
circle = pygame.image.load('circle.png')
cross = pygame.image.load('cross.png')

#display board
screen.blit(board,(0,0))
pygame.display.flip()

#variables that store the state of the game
game_over = False
which_symbol = 'circle'
board_state = [[' ',' ',' '],
			   [' ',' ',' '],
			   [' ',' ',' ']]

#function to check for matches in a straight line
def check_match():
	#horizontal match
	for i in range(3):
		if not board_state[i][0]==' ' and len(set(board_state[i]))==1:
			pygame.draw.line(screen,(0,0,0),(0,i*200+95),(599,i*200+95),10)
			return True
	#vertical match
	board_inverse_state = list(zip(*board_state))
	for i in range(3):
		if not board_inverse_state[i][0]==' ' and len(set(board_inverse_state[i]))==1:
			pygame.draw.line(screen,(0,0,0),(i*200+95,0),(i*200+95,599),10)
			return True
	#left diagonal
	if not board_state[0][0]==' ' and board_state[0][0]==board_state[1][1] and board_state[1][1]==board_state[2][2]:
		pygame.draw.line(screen,(0,0,0),(0,0),(599,599),10)
		return True
	#right diagonal
	if not board_state[2][0]==' ' and board_state[2][0]==board_state[1][1] and board_state[1][1]==board_state[0][2]:
		pygame.draw.line(screen,(0,0,0),(599,0),(0,599),10)
		return True
	return False

#game loop
clock = pygame.time.Clock()
while True:
	clock.tick(30)
	if not game_over:
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				mouse = pygame.mouse.get_pos()
				grid_x = mouse[0] // 200
				grid_y = mouse[1] // 200
				if board_state[grid_y][grid_x] == ' ':
					if which_symbol=='circle':
						board_state[grid_y][grid_x] = 'o'
						X = grid_x * 200 + 25
						Y = grid_y * 200 + 25
						#TODO: draw a circle at location (X,Y)
						print('draw a circle at location (X,Y)')
						screen.blit(circle,(X,Y))
						pygame.display.flip()
						game_over = check_match()
						pygame.display.flip()
						which_symbol = 'cross'
					elif which_symbol=='cross':
						board_state[grid_y][grid_x] = 'x'
						X = grid_x * 200 + 25
						Y = grid_y * 200 + 25
						#TODO: draw a cross at location (X,Y)
						print('draw a cross at location (X,Y)')
						screen.blit(cross,(X,Y))
						game_over = check_match()
						pygame.display.flip()
						which_symbol = 'circle'
#	else:
#		pygame.quit()
	
