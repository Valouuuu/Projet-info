import pygame
import fonctions as f
from pygame.locals import *
from cartes import Cartes
c = Cartes()

# pygame.init()

# window = pygame.display.set_mode((f.screen_size('x'),f.screen_size('y')-60))
# pygame.display.set_caption('Vélonimo')

# loop = True
# while loop :
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             loop = False

# pygame.quit()

deck = [1,9,28,36,5,23,47]

conv_deck = []

for i in range (0, len(deck)):
    conv_deck = conv_deck + c.color_card(deck[i]) + c.value_card(deck[i])
