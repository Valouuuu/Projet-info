import random

# J'ai rajouté une autre classe joueur pour différencier les comptes des joueurs avec les joueurs de la partie en cours 

class player ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.main = []
        
# Là je fais la liste que j'ai remplie de dico pour pouvoie asocier couleur et valeur mais en vrai go le refaire avec un "tableau de conversion", 
# ça sera plus simple

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

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

for p in player_list:
    print(p.main)

# Code de 3 à 5 joueurs

playing = 0


 
u = True



print("C'est au joueur",playing,"de jouer !")
print("Voici votre main")
print(player_list[playing].main)
print("Quelle(s) carte(s) voulez-vous jouer ?")

# On créer une boucle qui correspond au à la partie (ajouter boucle manche, tour, tour de joueur)

while u == True :
    color_list = []
    value_list = []
    count = 0
    center = 0  
    # Dans la boucle tour de joueur, ici on demande au joueur les cartes qu'il veut jouer
    for i in range (0,7):
        color = str(input("Saisir la couleur de la carte :"))
        value = str(input("Saisir la valeur de la carte :"))
        color_list.append(color) # On ajoute les couleurs de carte à une liste pour pouvoir les comparer
        value_list.append(value) # On ajoute les valeurs de carte à une liste pour pouvoir les comparer 
        
        for j in range (len(value_list)): # On cherche à trouver la valeur minimum présente dans la liste des valeurs
            if value_list[j] < value_list[j+1]:
                min = j
        
        for k in range (len(value_list)): # On compare les valeurs entre elles pour savoir si le joueur à jouer QUE des cartes de même valeur
            if value_list[k] == value_list(k+1): 
                count = count + 1
        
        if count == len(value_list): # Si on a bien des cartes de même valeur alors on fait le calcul de la valeur totale des cartes
            add_value = len(value_list)*10 + value_list[0]
        
        for k2 in range (len(color_list)): # On compare les couleurs entre elles pour savoir si le joueur à jouer QUE des cartes de même couleur
            if value_list[k2] == value_list(k2+1):
                count = count + 1
        
        if count == len(color_list): # Si on a bien des cartes de même couleur alors on fait le calcul de la valeur totale des cartes
            add_value = len(value_list)*10 + value_list[min]