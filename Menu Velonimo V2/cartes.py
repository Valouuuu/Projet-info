from mysql.connector import connect
import pygame
import random
import fonctions as f 
from db_handler_game import Db_Handler_Game
import button


db_handler_game = Db_Handler_Game()


def convert_card_button(deck_joueur: list):
    
    button_card_list = []
    
    for carte in deck_joueur :
        
        tuple = db_handler_game.image(carte)
        
        nom_carte = tuple[0]
        
        button_card_list.append(pygame.image.load('Jeu/images_cartes/'+ str(nom_carte)).convert())
    
    return button_card_list






def afficher_deck(window ,deck : list,j : int,x : int,y : int): # Ici on veut afficher la main du joueur (avec des coordonnées pour placer la main dans l'écran)
    
    a = -1
    
    for card in deck: # On parcourt la main 
        a = a + 1
        position_x = x + 80*a # On met à jour la position de la carte en x
        position_y = y # On met à jour la position de la carte en y
        if button.Button(position_x, position_y, card , 1).draw(window) :# On afficher la carte aux coordonées souhaitées pour la première cartes puis en décalé 
            pass
            
        
        
    
        
        
def afficher_mains_dos_cartes(window): # Affiche les mains cachées des joueurs qui ne jouent pas 
    
    carte_dos = pygame.image.load('Jeu/images_cartes/card_back.png').convert()
  
    # On affiche les cartes au dos, à gauche 
    #On ulisite la même structure à gauche, en haut et à droite
    a = 0
    carte_dos = pygame. transform. rotate (carte_dos, 90) # On tourne la carte encore de 90° vers la droite 
    for i in range (11):
        
        window.blit(carte_dos,(f.screen_size('x') - 260 , 100 + 40*a)) # On affiche les cartes une part une de la même façon que pour afficher les mains
        a = a + 1
    
    a = 0 
    carte_dos = pygame. transform. rotate (carte_dos, 90) # On tourne la carte encore de 90° vers la droite   
    for i in range (11):
         
        window.blit(carte_dos,(300 + 80*a , 0 )) # On affiche les cartes une part une de la même façon que pour afficher les mains
        a = a + 1
      
    a = 0 
    carte_dos = pygame. transform. rotate (carte_dos, 90) # On tourne la carte de 90° vers la droite 
    for i in range (11):
        
        window.blit(carte_dos,(0 , 100 + 40*a)) # On affiche les cartes une part une de la même façon que pour afficher les mains
        a = a + 1
    



