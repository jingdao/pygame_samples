import pygame
from pygame.locals import *

#initialize game window
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#load ball image
ball = pygame.image.load('ball.png')
ball_width = ball.get_rect().width
ball_height = ball.get_rect().height

#constant parameters
mass = 1.0
initial_height = 800
initial_velocity = 5
coefficient_of_restitution = 0.9
gravity = 9.8
initial_energy = mass * gravity * initial_height

#variable parameters
velocity_x = initial_velocity
velocity_y = 0
position_x = 0
position_y = initial_height
dissipated_energy = 0
rest = False

#timing parameters
fps = 30.0
dt = 0.5

def draw_ball(x, y):
	screen.fill((0,0,0))
	screen.blit(ball,(x,y))
	pygame.display.flip()

#game loop
clock = pygame.time.Clock()
while True:
	clock.tick(fps)
	position_x += velocity_x
	if rest:
		position_y = ball_height
	else:
		velocity_y -= gravity * dt
		kinetic_energy = 0.5 * mass * velocity_y**2
		potential_energy = initial_energy - kinetic_energy - dissipated_energy
		position_y = potential_energy / (mass * gravity)
	if position_x < 0 or position_x + ball_width > screen_width:
		velocity_x = -(velocity_x * coefficient_of_restitution)
	if position_y - ball_height < 10:
		dissipated_energy += (1-coefficient_of_restitution**2) * kinetic_energy
		velocity_y = -(velocity_y * coefficient_of_restitution)
		if abs(velocity_y) < 2:
			rest = True
	draw_ball(position_x, screen_height - position_y)
