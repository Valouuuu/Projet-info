import pygame
import button
from main_game import Game

pygame.init()

#create game window
screen = pygame.display.set_mode((0,0)) #on a mit (0,0) pour afficher le jeu en plein écran #sur mon écran l'image n'est pas bien centrée (quand la résolution est différentes, les images et boutons sont souvents mal placés)
pygame.display.set_caption("Velonimo")

game = Game(screen)

game.loop()

#close game window
pygame.quit()