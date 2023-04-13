import random
import player_turn
import turn


# J'ai rajouté une autre classe joueur pour différencier les comptes des joueurs avec les joueurs de la partie en cours 

class Joueur ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.deck = []
        self.points = 0
    def points(self, points_gagnés):
        self.points += points_gagnés
        
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]



# player_list = []

# On initialise les mains

# for b in range(a):
#     player_list.append(Joueur(b))

# On mélange la liste pour mélanger les cartes

# random.shuffle(list)   

# On distribue les cartes 

# for q in range (11): 
#     for p in player_list:
#         p.deck.append(list[0])
#         del(list[0])

# for p in player_list:
#     print(p.deck)

# Code de 3 à 5 joueurs

playing = 0


 
u = True



# print("C'est au joueur",playing,"de jouer !")
# print("Voici votre main")
# print(player_list[playing].deck)
# print("la pioche est :",list)

# On créé une boucle qui correspond au à la partie (ajouter boucle manche, tour, tour de joueur)


def manche(akiletour, player_list,):
    player_order = akiletour(player_list) #ordre des joueurs
    winner_order = player_order #initialisation du premier joueur
    for k in range (5): #boucle de la manche
        winner_order = turn(player_list, player_turn, winner_order[1], player_order) #ordre des gagnants
        for p in player_list: #distributions des points à la fin du tour
            for i in range(len(player_list)):
                if p == winner_order[i]:
                    p.points(k+1)
        
        


def akiletour(player_list): #créé un ordre des joueurs aléatoire 
    a = int(input("Veuillez rentrer le nombre de joueurs : "))
    player_list = []
    for b in range(a):
        player_list.append(Joueur(b))
    l = []
    for p in player_list:
        l += player_list[p]
    random.shuffle(l)
    for q in range (11): 
        for p in player_list:
            p.deck.append(list[0])
            del(list[0])
    return l