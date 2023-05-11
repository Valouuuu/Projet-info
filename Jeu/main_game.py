import pygame
import fonctions as f
from pygame.locals import *
import cartes as c


white = (255,255,255)

pygame.init()

window = pygame.display.set_mode((f.screen_size('x'),f.screen_size('y')-60))
pygame.display.set_caption('Vélonimo')

decks_list = c.init_deck()



loop = True

while loop :
    window.fill(white) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
    c.afficher_deck(window,decks_list,1,200,f.screen_size('y')-350)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
