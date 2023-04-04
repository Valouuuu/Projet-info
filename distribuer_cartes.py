import random
from joueur import Joueur

# Là je fais la liste que j'ai remplie de dico pour pouvoie asocier couleur et valeur mais en vrai go le refaire avec un "tableau de conversion", 
# ça sera plus simple

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

a = int(input("Veuillez rentrer le nombre de joueurs : "))

player_list = []

# On initialise les mains

for b in range (a):
    player_list.append(Joueur(b))

# On mélange la liste pour mélanger les cartes

random.shuffle(list)   

# On distrubue les cartes 

for q in range (0,11*a,a): 
    b=0
    for p in player_list:
        p.main.append(list[q+b])
        b += 1

for p in player_list:
    print(p.main)
    
# Le programme fonctionne, par contre on a juste un problème avec la classe, 
# il faudrait que les autres paramètre de la classe Joueur soient muettes