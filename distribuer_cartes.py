import random

# Classe joueur déjà faite mais faut ajouter ces self du coup
# Classe joueur pour tester le programme
class player ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.main = []

# Là je fais la liste que j'ai remplie de dico pour pouvoie asocier couleur et valeur mais en vrai go le refaire avec un "tableau de conversion", 
# ça sera plus simple

list = [{"red" : 1} , {"red" : 2} , {"red" : 3} , {"red" : 4} , {"red" : 5} , {"red" : 6} , {"red" : 7}, 
         {"blue" : 1} , {"blue" : 2} , {"blue" : 3} , {"blue" : 4} , {"blue" : 5} , {"blue" : 6} , {"blue" : 7} ,
         {"green" : 1}, {"green" : 2}, {"}green" : 3}, {"green" : 4}, {"green" : 5}, {"green" : 6}, {"green" : 7},
         {"yellow" : 1}, {"yellow" : 2}, {"yellow" : 3}, {"yellow" : 4}, {"yellow" : 5}, {"yellow" : 6}, {"yellow" : 7},
         {"pink" : 1}, {"pink" : 2}, {"pink" : 3}, {"pink" : 4}, {"pink" : 5}, {"pink" : 6}, {"pink" : 7},
         {"grey" : 1} , {"grey" : 2}, {"grey" : 3}, {"grey" : 4}, {"grey" : 5}, {"grey" : 6}, {"grey" : 7},
         {"brown" : 1}, {"brown" : 2}, {"brown" : 3}, {"brown" : 4}, {"brown" : 5}, {"brown" : 6}, {"brown" : 7},
         {"baroudeur" : 25}, {"baroudeur" : 30}, {"baroudeur" : 35}, {"baroudeur" : 40}, {"baroudeur" : 45}, {"baroudeur" : 50} ]

a = int(input("Veuillez rentrer le nombre de joueurs : "))

player_list = []

# On initialise les mains

for b in range (a):
    player_list.append(player(b))

# On mélange la liste pour mélanger les cartes

random.shuffle(list)   

# On distrubue les cartes 

for q in range (0,11*a,a): 
    b=0
    for p in player_list:
        p.main.append(list[q+b])
        b += 1

# Boucle pour afficher les mains 
# for p in player_list:
#     print(p.main)