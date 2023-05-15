from mysql.connector import connect
import pygame
import random
import fonctions as f 


# class Cartes():

#     def __init__(self):
#         self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")
#         self.deck = []
#     # Méthode pour mélanger les cartes
#     def Shuffle():
        
#         list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#         ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
#         ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

#         a = 3 # Correspond au nombre de joueurs, à récupérer avant de lancer la partie 

#         player_list = []

#         # On initialise les mains

#         for b in range(a):
#             player_list.append(Joueur(b))

#         # On mélange la liste pour mélanger les cartes

#         random.shuffle(list)   

#         # On distribue les cartes 

#         for q in range (11): 
#             for p in player_list:
#                 p.deck.append(list[0])
#                 del(list[0])

#         # for p in player_list:
#         #     print(p.deck)

#     # Méthode pour pour récupérer la couleur d'une carte
#     def color_card(self, card_id):
            
#             cursor = self.con.cursor()
#             query = "SELECT car_color FROM Cartes WHERE car_id = %s;"
#             cursor.execute(query, (card_id,))
#             result = cursor.fetchall()
#             cursor.close()
            
#             return result


#        # Méthode pour pour récupérer la valeur d'une carte
#     def value_card(self, card_id):
            
#             cursor = self.con.cursor()
#             query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
#             cursor.execute(query, (card_id,))
#             result = cursor.fetchall()
#             cursor.close()
            
#             return result

 # def value_card(self, deck):

    #     final_list = []
        
    #     for i in range (0,7):
    #         a = str(deck[i])
    #         cursor = self.con.cursor()
    #         query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
    #         cursor.execute(query, (a,))
    #         result = cursor.fetchall()
    #         cursor.close()
            
    #         final_list = final_list + result
        
    #     return final_list

class Cartes():
    
    def __init__(self,x,y,couleur,valeur): # On créé les cartes avec les paramètres couleur, valeur et le code qui permet d'afficher l'image de la carte 
        self.couleur = couleur
        self.valeur = valeur
        self.image = pygame.image.load('Jeu/images_cartes/card_'+ valeur + '_' + couleur +'.png').convert() 
        self.rect = self.image.get_rect()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self, surface):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action




def creer_cartes(couleur,nb_cartes, liste_des_cartes): #Ici on créer les cartes d'une même couleur, on prend en paramètre la couleur qu'on veut créer et la liste dans laquelle se trouvera toutes les cartes 
    
    for i in range (1, nb_cartes + 1): # on fait une boucle pour ajouter les objets cartes dans une liste qui contiendra toutes les cartes 
        
        liste_des_cartes.append(Cartes(couleur,str(i))) 
        
    return liste_des_cartes # Retourne la liste des cartes de la couleur demandée au nombre demandé
 
 
def create_all_cards(): # Ici la fonction permet de créer toutes les cartes du jeu et de les stocker dans la liste all_cards
    
    # On aura besoin de retirer le dernier element 'None' de la liste à chaque fois 
    all_cards = []
    all_cards.append(creer_cartes('baroudeur',6,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('red',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('blue',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('green',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('yellow',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('brown',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('pink',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    all_cards.append(creer_cartes('grey',7,all_cards))
    del(all_cards[len(all_cards) - 1])
    

    return all_cards # Retourne la liste des cartes 


def init_decks(cartes): # Cette fonction permet d'innitialiser les main des joueur de manière aléatoire

    player_deck = [] # liste contenant les mains des joueurs
    
    random.shuffle(cartes) # On mélange la liste des cartes pour mélanger les cartes

    for i in range (4): # On distribue les cartes pour le nombre de joueur souhaité, ici 4
        deck = [] # On créer une liste qui sera la main du joueur 
        for j in range (11): # On fait une boucle correpondant au nombre de cartes par main, ici 11
            deck.append(cartes[j]) # On ajoute le permier élément de la liste des cartes qui a été mélangée
            del(cartes[j]) # On supprime de la liste des cartes la carte qu'on vient d'ajouter 
        player_deck.append(deck) # une fois la boucle finie, on ajoute la main à la liste des mains des joueurs

    
    return player_deck # On retourne la liste complète des main des joueurs 


def afficher_deck(window,deck_list,j,x,y): # Ici on veut afficher la main du joueur (avec des coordonnées pour placer la main dans l'écran)
    # On a pris en paramètre la liste qui contenait toutes les main des joueurs (qui sont des listes),
    # j qui est le joueur à qui on doit afficher sa main
    deck_display = deck_list[j-1] # Ici on récupère la première liste (la prmière main qu'on veut afficher) pour la parcourir 
    a = 0
    for i in deck_display: # On parcourt la main (i est un objet)
        
        window.blit(i.image,(x + 80*a, y)) # On afficher la carte aux coordonées souhaitées pour la première cartes puis en décalé 
        i.position_x = x + 80*a # On met à jour la position de la carte en x
        i.position_y = y # On met à jour la position de la carte en y
        a = a + 1
        
        
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
    



