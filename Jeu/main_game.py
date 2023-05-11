import pygame
import fonctions as f
from pygame.locals import *
from cartes import Cartes
c = Cartes()

white = (255,255,255)

pygame.init()

window = pygame.display.set_mode((f.screen_size('x'),f.screen_size('y')-60))
pygame.display.set_caption('Vélonimo')

carte_1_blue = pygame.image.load('Jeu/images_cartes/card_1_blue.png').convert()
carte_2_blue = pygame.image.load('Jeu/images_cartes/card_2_blue.png').convert()
carte_3_blue = pygame.image.load('Jeu/images_cartes/card_3_blue.png').convert()
carte_4_blue = pygame.image.load('Jeu/images_cartes/card_4_blue.png').convert()
carte_5_blue = pygame.image.load('Jeu/images_cartes/card_5_blue.png').convert()
carte_6_blue = pygame.image.load('Jeu/images_cartes/card_6_blue.png').convert()
carte_7_blue = pygame.image.load('Jeu/images_cartes/card_7_blue.png').convert()
carte_1_red = pygame.image.load('Jeu/images_cartes/card_1_red.png').convert()
carte_2_red = pygame.image.load('Jeu/images_cartes/card_2_red.png').convert()
carte_3_red = pygame.image.load('Jeu/images_cartes/card_3_red.png').convert()
carte_4_red = pygame.image.load('Jeu/images_cartes/card_4_red.png').convert()
carte_5_red = pygame.image.load('Jeu/images_cartes/card_5_red.png').convert()
carte_6_red = pygame.image.load('Jeu/images_cartes/card_6_red.png').convert()
carte_7_red = pygame.image.load('Jeu/images_cartes/card_7_red.png').convert()
carte_1_green = pygame.image.load('Jeu/images_cartes/card_1_green.png').convert()
carte_2_green = pygame.image.load('Jeu/images_cartes/card_2_green.png').convert()
carte_3_green = pygame.image.load('Jeu/images_cartes/card_3_green.png').convert()
carte_4_green = pygame.image.load('Jeu/images_cartes/card_4_green.png').convert()
carte_5_green = pygame.image.load('Jeu/images_cartes/card_5_green.png').convert()
carte_6_green = pygame.image.load('Jeu/images_cartes/card_6_green.png').convert()
carte_7_green = pygame.image.load('Jeu/images_cartes/card_7_green.png').convert()
carte_1_pink = pygame.image.load('Jeu/images_cartes/card_1_pink.png').convert()
carte_2_pink = pygame.image.load('Jeu/images_cartes/card_2_pink.png').convert()
carte_3_pink = pygame.image.load('Jeu/images_cartes/card_3_pink.png').convert()
carte_4_pink = pygame.image.load('Jeu/images_cartes/card_4_pink.png').convert()
carte_5_pink = pygame.image.load('Jeu/images_cartes/card_5_pink.png').convert()
carte_6_pink = pygame.image.load('Jeu/images_cartes/card_6_pink.png').convert()
carte_7_pink = pygame.image.load('Jeu/images_cartes/card_7_pink.png').convert()
carte_1_grey = pygame.image.load('Jeu/images_cartes/card_1_grey.png').convert()
carte_2_grey = pygame.image.load('Jeu/images_cartes/card_2_grey.png').convert()
carte_3_grey = pygame.image.load('Jeu/images_cartes/card_3_grey.png').convert()
carte_4_grey = pygame.image.load('Jeu/images_cartes/card_4_grey.png').convert()
carte_5_grey = pygame.image.load('Jeu/images_cartes/card_5_grey.png').convert()
carte_6_grey = pygame.image.load('Jeu/images_cartes/card_6_grey.png').convert()
carte_7_grey = pygame.image.load('Jeu/images_cartes/card_7_grey.png').convert()
carte_1_brown = pygame.image.load('Jeu/images_cartes/card_1_brown.png').convert()
carte_2_brown = pygame.image.load('Jeu/images_cartes/card_2_brown.png').convert()
carte_3_brown = pygame.image.load('Jeu/images_cartes/card_3_brown.png').convert()
carte_4_brown = pygame.image.load('Jeu/images_cartes/card_4_brown.png').convert()
carte_5_brown = pygame.image.load('Jeu/images_cartes/card_5_brown.png').convert()
carte_6_brown = pygame.image.load('Jeu/images_cartes/card_6_brown.png').convert()
carte_7_brown = pygame.image.load('Jeu/images_cartes/card_7_brown.png').convert()
carte_1_yellow = pygame.image.load('Jeu/images_cartes/card_1_yellow.png').convert()
carte_2_yellow = pygame.image.load('Jeu/images_cartes/card_2_yellow.png').convert()
carte_3_yellow = pygame.image.load('Jeu/images_cartes/card_3_yellow.png').convert()
carte_4_yellow = pygame.image.load('Jeu/images_cartes/card_4_yellow.png').convert()
carte_5_yellow = pygame.image.load('Jeu/images_cartes/card_5_yellow.png').convert()
carte_6_yellow = pygame.image.load('Jeu/images_cartes/card_6_yellow.png').convert()
carte_7_yellow = pygame.image.load('Jeu/images_cartes/card_7_yellow.png').convert()
carte_25_baroudeur = pygame.image.load('Jeu/images_cartes/card_25_baroudeur.png').convert()
carte_30_baroudeur = pygame.image.load('Jeu/images_cartes/card_30_baroudeur.png').convert()
carte_35_baroudeur = pygame.image.load('Jeu/images_cartes/card_35_baroudeur.png').convert()
carte_40_baroudeur = pygame.image.load('Jeu/images_cartes/card_40_baroudeur.png').convert()
carte_45_baroudeur = pygame.image.load('Jeu/images_cartes/card_45_baroudeur.png').convert()
carte_50_baroudeur = pygame.image.load('Jeu/images_cartes/card_50_baroudeur.png').convert()

decks_list = f.init_deck()

loop = True
while loop :
    window.fill(white) 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            loop = False
    f.afficher(window,decks_list,1,300,f.screen_size('y')-350)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()



    
    