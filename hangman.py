import pygame
from pygame.locals import *
import random

#initialize game window
pygame.init()
screen = pygame.display.set_mode((800,400))
screen.fill((255,255,255))

#load dictionary words
f = open('dictionary.txt','r')
words = f.read().split('\n')
secret_id = random.randint(0,len(words)-1)
secret_word = words[secret_id]
print(secret_word)
revealed = [False]*len(secret_word)
wrong_guesses = 0

#import image resources
hang_images = [
	pygame.image.load('hang_0.png'),
	pygame.image.load('hang_1.png'),
	pygame.image.load('hang_2.png'),
	pygame.image.load('hang_3.png'),
	pygame.image.load('hang_4.png'),
	pygame.image.load('hang_5.png'),
	pygame.image.load('hang_6.png'),
]
font = pygame.font.Font(None, 50)

def update_screen():
	screen.fill((255,255,255))
	screen.blit(hang_images[wrong_guesses], (0,0))
	s = ''
	for i in range(len(secret_word)):
		if revealed[i]:
			s += secret_word[i]+' '
		else:
			s += '_ '
	text = font.render(s, True, (0,0,0))
	rect = text.get_rect()
	rect.center = (400,350)
	screen.blit(text, rect)
	pygame.display.flip()
update_screen()

#game loop
game_over = False
clock = pygame.time.Clock()
while True:
	clock.tick(30)
	if not game_over:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key >= K_a and event.key <= K_z:
					input_character = chr(event.key - K_a + ord('A'))
					print(input_character)
					correct = False
					for i in range(len(secret_word)):
						if secret_word[i] == input_character:
							revealed[i] = True
							correct = True
					if not correct:
						wrong_guesses += 1
					update_screen()
					if all(revealed):
						print('GAME OVER (you win)!!!')
						game_over = True
					if wrong_guesses == 6:
						print('GAME OVER (you lose)!!!')
						game_over = True

