import random
from db_handler_game import Db_Handler_Game

db_handler = Db_Handler_Game()

class Joueur():
    
    def __init__ (self, joueur):
        
        self.numero_joueur = joueur # Le numéro de joueur
        # self.pseudo = pseudo    # Nom du joueur (amélioration)
        self.deck = []  # Main du joueur 
        self.points = 0 # Nombre de points du joueur 
        self.a_mon_tour = False # Permet de savoir si c'est au joueur de jouer
        self.combinaison = [] # Combinaison en cours
    
    # Méthode pour compter le nombre de points
    def calcul_points(self, points_gagnés):
        self.points += points_gagnés

    # Méthode pour vérifié si la combinaison de carte est valide, et savoir de quelle combinaison il s'agit (couleur ou valeur)   
    def verif_combi(self): # On prend en paramètre les cartes sélectionnées 
        
        verif = False # On initialise la vérification 
        
        compteur_1 = 0 # On initialise le premier compteur 
        compteur_2 = 0 # On initialise le deuxième compteur
        
        for i in range(1,len(self.combinaison)) : # Ici on vérifie pour toutes les cartes de la liste 
            
            if db_handler.value(self.combinaison[i]) == db_handler.value(self.combinaison[i + 1]) : # Si la carte i a la même valeur que celle d'après 
                compteur_1 = compteur_1 + 1 # Dans ce cas on ajoute 1 au compteur 
            
            if db_handler.color(self.combinaison[i]) == db_handler.color(self.combinaison[i + 1]) :# Si la carte i a la même couleur que celle d'après 
                compteur_2 = compteur_2 + 1 # Dans ce cas on ajoute 1 au compteur
            
        if compteur_1 == len(self.combinaison)  or compteur_2 == len(self.combinaison): # Ici on vérifie que le compteur a la même valeur que la longeur de la liste
            vérif = True # Dans ce cas la main est vérifiée 
            
        if compteur_1 == len(self.combinaison): # Ici on regarde si c'est une combinaison de valeur 
            return [verif,'value'] # On retourne valeur 
        
        if compteur_2 == len(self.combinaison) : # Ici on regarde si c'est une combinaison de couleur  
            return [verif,'color'] # On retourne couleur
    
    
    def calculer_combinaison(self, verif_combi): # On prend en paramètre la liste des cartes selectionnées (liste d'entiers)
        
        value_combinaison = 0 # On initialise la valeur de la combinaison 
        verif_comb = verif_combi(self.combinaison) # On vérifie la combinaison et on récupère le type de combinaison
        value_petite_carte = 0 # On initialise la valeur de la plus petite carte
        
        if verif_comb[0] == True : # Si la combinaison est vérifiée
            for i in (1, len(self.combinaison)): # On compare toutes les cartes de la combinaison 
                if db_handler.value(self.combinaison[i]) < db_handler.value(self.combinaison[i + 1]): # On regarde quelle est la plus petite valeur de la combinaison (pour une combinaison de valeur on pourrait directement prendre la valeur de n'importe quelle carte )
                    value_petite_carte = db_handler.value(self.combinaison[i]) # On la définit comme étant la plus petite valeur 
                
            # On calcule la valeur de la combinaison (au final on est pas obligé de distinguer les cas 'couleur' 'valeur')
            if verif_comb[1] == 'value' : 
                value_combinaison = len(self.combinaison)*10 + value_petite_carte
            
            if verif_comb[1] == 'color' :
                value_combinaison = len(self.combinaison)*10 + value_petite_carte
     
    # Méthode pour valider la combinaison, pour la poser au centre              
    def bonne_combi(self, center_value : int, calculer_value, verif_combi):
        
        if calculer_value(self.combinaison) > center_value : # On regarde si la valeur de la combinaison est supérieure à celle du centre 
            
            return True # on renvoit Vrai
    
# Fonction pour reset le compteur pour savoir qui doit jouer 
def ordre_passage(a_qui_de_jouer : int): # On prend en paramètre qui doit jouer      
    if a_qui_de_jouer >= 5 : # On regarde si le compteur va au dessus de 4 (4 joueurs)
        return 1 # On réinitialise le à qui de jouer au premier joueur 

    
        
                
                
        
           
            
        
def deckplayer(nbreplayer : int):
    
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
            ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
            ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

    # Liste contenant les objets joueurs
    player_list = []

    #On initialise les mains
    for b in range(nbreplayer): # Selon le nombre de joueurs, on le fixe à 4
        player_list.append(Joueur(b)) # On remplit notre liste de joueurs avec les objets joueurs  

    # On mélange la liste pour mélanger les cartes
    random.shuffle(list)   

    # On distribue les cartes 
    for q in range (11):  # Une main contient 11 cartes 
        for p in player_list:  # Pour chaque joueurs 
            p.deck.append(list[0]) # On ajoute des cartes dans les decks des joueurs
            del(list[0]) # On supprime la carte qu'on vient d'ajouter pour avoir la liste des cartes restantes si besoin
    
    return player_list