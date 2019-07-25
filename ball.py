import pygame
from pygame.locals import *

#initialize game window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#load bedroom image
bedroom = pygame.image.load('bedroom.png')

#load ball image
ball = pygame.image.load('ball.png')
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height

#constant parameters
initial_velocity = 5
coefficient_of_restitution = 0.9
gravity = 9.8

#variable parameters
velocity_x = initial_velocity
velocity_y = 0
position_x = 0
position_y = 0
rest = False

#timing parameters
fps = 20.0

def draw_ball(x, y):
	screen.blit(bedroom, (0,0))
	screen.blit(ball,(x,y))
	pygame.display.flip()

#game loop
clock = pygame.time.Clock()
while True:
	clock.tick(fps)
	position_x += velocity_x
	if rest:
		position_y = screen_height - ball_height
	else:
		velocity_y += gravity
		position_y += velocity_y
	if position_x < 0 or position_x + ball_width > screen_width:
		velocity_x = -(velocity_x * coefficient_of_restitution)
	if position_y + ball_height > 725:
		velocity_y = -(velocity_y * coefficient_of_restitution)
		if abs(velocity_y) < 2:
			rest = True
	print('x',position_x,'y',position_y,'vx',velocity_x,'vy',velocity_y)
	draw_ball(position_x, position_y)
