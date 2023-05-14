import pygame
import fonctions as f
from pygame.locals import *
import cartes as c
import event as e

black = (0,0,0) # On définit la couleur blanc

pygame.init() # initialisation de pygame

window = pygame.display.set_mode((f.screen_size('x'),f.screen_size('y')-60)) # On initialise la fenêtre à la taille de l'écran
pygame.display.set_caption('Vélonimo') # On l'appelle 'Vélonimo'

liste_des_cartes = c.create_all_cards() # On créé la liste des cartes 
decks_list = c.init_deck(liste_des_cartes) # On initialise les mains

joueur = 1

loop = True
x=0
y=0
c.afficher_mains_dos_cartes(window) # Affiche les mains des joueurs qui ne jouent pas 
c.afficher_deck(window , decks_list , joueur , 300 , f.screen_size('y')-350) # Affiche la main du premier joueur 

deck_en_cours = decks_list [ joueur -1 ]
e.motion(window , deck_en_cours ,black)
    
while loop :
    
    # window.fill(white) # On rempli le fond d'écran en blanc
    
    
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            loop = False
                 
        
        
        if event.type == MOUSEBUTTONDOWN :
                
            x, y = event.pos
            
            if pygame.mouse.get_pressed()[0] == 1 :
                
                for carte in deck_en_cours :
                    
                    if carte.selected == False :
                        rectangle = pygame.draw.rect(window,black,(carte.position_x , carte.position_y , 187 - 107 , 260))
                        window.blit(carte.image,(carte.position_x  , carte.position_y))
                        
                        if rectangle.collidepoint(x,y) and carte.selected == False :
                            carte.selected = True
                            window.blit(carte.image,(carte.position_x , carte.position_y - 50))
                            pygame.draw.rect(window,black,(carte.position_x , carte.position_y - 50 + 260 , 187  , 50))
                            break
                        
                
        
            
            
    
    
    pygame.display.flip()
    pygame.display.update() # Permet de mettre à jour les actions sur l'écran
pygame.quit()
