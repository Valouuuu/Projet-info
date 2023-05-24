import random
import player_turn
import turn


# J'ai rajouté une autre classe joueur pour différencier les comptes des joueurs avec les joueurs de la partie en cours 

class Joueur ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.deck = []
        self.points = 0
    def score(self, points_gagnés):
        self.points += points_gagnés
        
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]



def manche(akiletour, player_list):
    player_order = akiletour(player_list) #ordre des joueurs
    winner = player_order[0] #initialisation du premier joueur
    for k in range (5): #boucle de la manche
        winner_order = turn(player_turn, winner_order[0], player_order) #ordre des gagnants
        player_list[winner_order[0]].score(k+1) #distributions des points à la fin du tour

def akiletour(player_list, nb_joueur): #créé un ordre des joueurs aléatoire 
    player_list = []
    for b in range(nb_joueur):
        player_list.append(Joueur(b))
    l = []
    for p in player_list:
        l += player_list[p]
    random.shuffle(l)
    return l