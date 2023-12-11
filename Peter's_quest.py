#Imports
import pygame
import sys
import random

pygame.init()

#Screen + Font
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Peter's quest")
screen.fill("white")

main_font = pygame.font.SysFont("Roboto", 90)

#Title
title = main_font.render("Peter's Quest", True, "black")
title_rect = title.get_rect(center=(485, 50))

#Play
play = main_font.render("New Game", True, 'black')
play_rect = play.get_rect(center=(485, 200))


"""#Battle
battle = main_font.render("A mangoos appeared!", True, 'black')
battle_rect = battle.get_rect(center=(485, 320))

#Between
between = main_font.render("Good job! What should you do to prepare for the next fight?", True, 'white')
between_rect = between.get_rect(center=(485, 340))
"""
#Best Score
best_scores = main_font.render("Best Scores", True, 'black')
best_scores_rect = best_scores.get_rect(center=(485, 280))

#Credits
cred = main_font.render("Credits", True, 'black')
cred_rect = cred.get_rect(center=(485, 360))

#Quit
q = main_font.render("Quit", True, 'black')
q_rect = q.get_rect(center=(485, 440))

#Game state
game_state = "Menu"




#Game Loop
while True:
    #Events and Buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #screen
    screen.fill("white")

    #Game State Logic
    if game_state == "Menu":
        screen.blit(title, title_rect)
        screen.blit(play, play_rect)
        screen.blit(cred, cred_rect)
        screen.blit(best_scores, best_scores_rect)
        screen.blit(q, q_rect)
        
    elif game_state == "Battle":
        screen.fill("white")
        screen.blit(battle, battle_rect)

    #Update display
    pygame.display.flip()



class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.transform.scale(button_surface, (400, 150))

play = Button("New game", 400, 300, "Button")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			play.checkForInput(pygame.mouse.get_pos())

	screen.fill("white")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()

