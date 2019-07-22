import pygame
from pygame.locals import *
import time

pygame.init()
button_size = 100
margin = 20
screen_width = 4 * button_size + 5 * margin
screen_height = 5 * button_size + 6 * margin

#initialize game window
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255,255,255))

#draw buttons as rectangles
pygame.draw.rect(screen, (0,0,0), Rect(margin, margin, 4*button_size+3*margin, button_size), 2)
for i in range(14):
	x = i % 4
	y = i // 4
	pygame.draw.rect(screen, (0,0,0), Rect(margin+x*(button_size+margin), margin+(y+1)*(button_size+margin), button_size, button_size), 2)
pygame.draw.rect(screen, (0,0,0), Rect(margin+2*(button_size+margin), margin+4*(button_size+margin), 2*button_size+margin, button_size), 2)

#draw numbers
font = pygame.font.Font('freesansbold.ttf', 50)
characters = ['7','8','9','C','4','5','6','+','1','2','3','x','0','.','=']
for i in range(15):
	x = i % 4
	y = i // 4
	text = font.render(characters[i], True, (0,0,0))
	rect = text.get_rect()
	if i==14:
		rect.center = (margin*7//2+button_size*3, margin+button_size//2+(y+1)*(button_size+margin))
	else:
		rect.center = (margin+button_size//2+x*(button_size+margin), margin+button_size//2+(y+1)*(button_size+margin))
	screen.blit(text, rect)

#function to display calculator output
def calculator_display(s):
	pygame.draw.rect(screen, (255,255,255), Rect(margin+2, margin+2, 4*button_size+3*margin-4, button_size-4), 0)
	text = font.render(s, True, (0,0,0))
	rect = text.get_rect()
	rect.center = (screen_width-margin*2-rect.width//2, margin+button_size//2)
	screen.blit(text, rect)
	pygame.display.flip()

#render everything to display
pygame.display.flip()

#calculator variables
previous_operand = ''
current_operand = ''
operator = None
def calculate():
	if operator=='+':
		result = float(previous_operand) + float(current_operand)
	elif operator=='x':
		result = float(previous_operand) * float(current_operand)
	else:
		return ''
	if int(result)==result:
		return str(int(result))
	else:
		return str(result)

#game loop
clock = pygame.time.Clock()
while True:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == MOUSEBUTTONUP:
			mouse = pygame.mouse.get_pos()
			grid_x = (mouse[0]-margin) // (button_size+margin)
			grid_y = (mouse[1]-margin*2-button_size) // (button_size+margin)
			character_idx = grid_y*4 + grid_x
			if character_idx>=0 and character_idx<=15:
				selected_character = characters[character_idx] if character_idx<15 else characters[14]
				print('Entered',selected_character)
				if selected_character.isdigit() or selected_character=='.':
					current_operand+=selected_character
					calculator_display(current_operand)
				elif selected_character in ['+','x']:
					if current_operand!='':
						if operator!=None:
							previous_operand = calculate()
						else:
							previous_operand = current_operand
						operator = selected_character
						calculator_display(previous_operand)
						current_operand = ''
				elif selected_character=='=':
					if previous_operand!='' and current_operand!='' and operator!=None:
						current_operand = calculate()
						calculator_display(current_operand)
						previous_operand = ''
						current_operand = ''
						operator = None
				elif selected_character=='C':
					previous_operand = ''
					current_operand = ''
					operator = None
					calculator_display(current_operand)

