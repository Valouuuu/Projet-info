import pygame
from cartes import Cartes
import random

def screen_size(size):
    screen_size  = pygame.display.get_desktop_sizes()
    tu = screen_size[0]
    x = tu[0]
    y = tu[1]
    if size == 'x':
        return x
    elif size == 'y':
        return y

pygame.init()

window = pygame.display.set_mode((screen_size('x'),screen_size('y')-60))
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


    
    
def afficher (window,decks_list,j,x,y):
    deck_display = decks_list[j-1]
    a=0
    for i in deck_display:
        window.blit(i,(x + 100*a, y))
        a+=1
    
def init_deck(): 
    
    # liste des cartes
    
    list = [ carte_1_blue, carte_2_blue, carte_3_blue, carte_4_blue, carte_5_blue, carte_6_blue, carte_7_blue,
            carte_1_green, carte_2_green, carte_3_green, carte_4_green, carte_5_green, carte_6_green, carte_7_green,
            carte_1_red, carte_2_red, carte_3_red, carte_4_red, carte_5_red, carte_6_red, carte_7_red, 
            carte_1_yellow, carte_2_yellow, carte_3_yellow, carte_4_yellow, carte_5_yellow, carte_6_yellow, carte_7_yellow, 
            carte_1_pink, carte_2_pink, carte_3_pink, carte_4_pink, carte_5_pink, carte_6_pink, carte_7_pink, 
            carte_1_brown,  carte_2_brown,  carte_3_brown,  carte_4_brown,  carte_5_brown,  carte_6_brown,  carte_7_brown,  
            carte_1_grey, carte_2_grey, carte_3_grey, carte_4_grey, carte_5_grey, carte_6_grey, carte_7_grey, 
            carte_25_baroudeur,  carte_30_baroudeur,  carte_35_baroudeur,  carte_40_baroudeur,  carte_45_baroudeur,  carte_50_baroudeur]

    # liste contenant les mains des joueurs
    
    player_list = []

    # On mélange la liste des cartes pour mélanger les cartes

    random.shuffle(list)   

    # On distribue les cartes 

    for i in range (4): 
        deck = []
        for j in range (11):
            deck.append(list[j])
            del(list[j])   
        player_list.append(deck)

    
    return player_list