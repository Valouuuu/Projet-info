import pygame
import button
from game import Game

pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Velonimo")

game = Game()

game.loop(screen)