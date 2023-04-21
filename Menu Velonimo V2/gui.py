import pygame
import button
from game import Game

pygame.init()

#create game window
screen = pygame.display.set_mode((0,0)) #on a mit (0,0) pour afficher le jeu en plein écran
pygame.display.set_caption("Velonimo")

game = Game()

game.loop(screen)