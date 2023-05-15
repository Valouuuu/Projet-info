class Joueur ():
    def __init__ (self,joueur):
        self.numero_joueur = joueur         
        self.deck = []
        self.points = 0
        self.à_mon_tour = False
    
    
    def points(self, points_gagnés):
        self.points += points_gagnés



import random

def deckplayer(nbreplayer):
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
            ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
            ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

    #init var
    player_list = []

    #Pour nbreplayer Joueur :
    for k in range(nbreplayer):
        player_list.append(k+1)
    print(player_list)

    #On initialise les mains
    for b in range(nbreplayer):
        player_list.append(Joueur(b))

    # On mélange la liste pour mélanger les cartes
    random.shuffle(list)   

    # On distribue les cartes 
    for q in range (11): 
        for p in player_list:
            p.deck.append(list[0])
            del(list[0])

    for p in player_list:
        print(p.deck)

deckplayer(4)