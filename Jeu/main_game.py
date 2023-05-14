import pygame
import fonctions as f
from pygame.locals import *
import cartes as c


white = (255,255,255)

pygame.init()

window = pygame.display.set_mode((f.screen_size('x'),f.screen_size('y')-60))
pygame.display.set_caption('Vélonimo')

liste_des_cartes = c.create_all_cards() # On créé la liste des cartes 
decks_list = c.init_deck(liste_des_cartes) # On initialise les mains



loop = True

while loop :
    window.fill(white) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
    c.afficher_mains_dos_cartes(window)
    c.afficher_deck(window,decks_list,1,300,f.screen_size('y')-350)
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()
