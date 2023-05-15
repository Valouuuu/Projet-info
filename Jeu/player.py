import random

class Joueur():
    
    def __init__ (self,pseudo,joueur):
        
        self.numero_joueur = joueur # Le numéro de joueur
        self.pseudo = pseudo    # Nom du joueur (améloration)
        self.deck = []  # Main du joueur 
        self.points = 0 # Nombre de points du joueur 
        self.à_mon_tour = False # Permet de savoir si c'est au joueur de jouer
    
    # Méthode pour compter le nombre de points
    def calcul_points(self, points_gagnés):
        self.points += points_gagnés
    
    # Méthode pour mélanger les cartes
    def shuffle():
        
        liste_cartes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
                ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
                38,39,40,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]
        
        random.shuffle(liste_cartes)
        
        return liste_cartes
        
    # Méthode pour initialister les decks
    def init_decks(self, liste_cartes : list):
        
        player_list = []
        nb_joueurs = 4 # On choisit de fixé le nombre de joueurs à 4, mais on laisse une variable pour la possipilité de jouer avec un autre nombre de joueurs (amélioration)
        
        # On initialise les mains
        for b in range(nb_joueurs): # Selon le nombre de joueurs
            player_list.append(Joueur(b)) # On remplit notre liste de joueurs avec les objets joueurs 

       
        # On distribue les cartes 
        for q in range (11): # Une main contient 11 cartes 
            for p in player_list: # Pour chaque joueurs 
                p.deck.append(liste_cartes[0]) # On ajoute des cartes dans les decks des joueurs
                del(liste_cartes[0]) # On supprime la carte qu'on vient d'ajouter pour avoir la liste des cartes restantes si besoin

            
