import random

# J'ai rajouté une autre classe joueur pour différencier les comptes des joueurs avec les joueurs de la partie en cours 

class Joueur ():
    def __init__ (self,pseudo):
        self.pseudo = pseudo             
        self.deck = []
        self.round = False
    def winner_last_round(self):
        self.round = True
        
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

a = int(input("Veuillez rentrer le nombre de joueurs : "))

player_list = []

# On initialise les mains

for b in range(a):
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

# Code de 3 à 5 joueurs

playing = 0


 
u = True



print("C'est au joueur",playing,"de jouer !")
print("Voici votre main")
print(player_list[playing].deck)
print("la pioche est :",list)

# On créé une boucle qui correspond au à la partie (ajouter boucle manche, tour, tour de joueur)




def player_turn(center,deck):
    while True :
        add_value = 0
        # Dans la boucle tour de joueur, ici on demande au joueur les cartes qu'il veut jouer
        print("Que souhaitez vous faire ?")
        print("1 : Jouer des cartes ")
        print("2 : Passer mon tour ")
        do = int(input(":"))
        n = int(input("Combien de cartes voulez-vous jouer ? :"))
        if do == 1 :    
            while add_value < center :  
                color_list = []
                value_list = []
                count = 0
                min = 51
                for i in range (n):
                    color = str(input("Saisir la couleur de la carte :"))
                    value = int(input("Saisir la valeur de la carte :"))
                    color_list.append(color) # On ajoute les couleurs de carte à une liste pour pouvoir les comparer
                    value_list.append(value) # On ajoute les valeurs de carte à une liste pour pouvoir les comparer 
                    
                if len(value_list) != 1:
                    for j in range (len(value_list)): # On cherche à trouver la valeur minimum présente dans la liste des valeurs
                        if value_list[j] < min :
                            min = j
                
                if value_list[0] != "baroudeur" and len(value_list) != 1:
                    
                    comp = value_list[0] # Valeur pour comparer dans la liste 
                    
                    for k in range (len(value_list)): # On compare les valeurs entre elles pour savoir si le joueur à jouer QUE des cartes de même valeur
                        if value_list[k] == comp : 
                            count =+ 1
                    
                    if count == len(value_list): # Si on a bien des cartes de même valeur alors on fait le calcul de la valeur totale des cartes
                        add_value = len(value_list)*10 + value_list[0]
                    
                    comp2 = color_list[0] # Valeur pour comparer la liste
                    
                    for k2 in range (len(color_list)): # On compare les couleurs entre elles pour savoir si le joueur à jouer QUE des cartes de même couleur
                        if color_list[k2] == comp2 :
                            count =+ 1
                    
                    if count == len(color_list): # Si on a bien des cartes de même couleur alors on fait le calcul de la valeur totale des cartes
                        add_value = n*10 + value_list[min]

                else :
                    if len(value_list) == 1 :
                        add_value = value_list[min]
                    else :
                        print("La combinaison n'est pas valide")

            if add_value > center : # Si la valeur totale de la main est supérieure à la valeur au centre, 
                center = add_value  # on pose la main et elle devient la nouvelle valeur du centre
                return center
            else :
                return False  
        else:
            False

              

def tour(player_list,winner):
    center = 0 #valeur du centre au début du tour
    # for p in player_list: #le gagnant de la dernière manche joue (sauf si c'est la 1ère manche le plus jeune)
    #     if p.
    while True: #boucle du tour
        playerking == 0
        for p in player_list: 
            if playerking != player_list[p]: #si le joueur n'est pas le king
                if not False : #si le joueur joue
                    center = player_turn(center,p.deck)
                    playerking = player_list[p]
            else : #fin du tour
               False
    return

def manche():
    for k in range (5):
        tour()


        