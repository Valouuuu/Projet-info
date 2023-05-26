from db_handler_game import Db_Handler_Game

db = Db_Handler_Game ()

def convert(deck: list):
    card_list = []
    
    for carte in deck :
        couleur_= db.color(carte)
        couleur = couleur_[0]
        valeur_= db.value(carte)
        valeur = valeur_[0]
        
        card_list.append([couleur,valeur])
        
    return card_list
        
def del_card(player,main: list,color: str,value: int):
    
    id_card_ = db.id(color,value)
    id_card = id_card_[0]
    i = 0
    for carte in main :
        if carte ==  id_card :
            del(main[i])
        i = i + 1
    
    player.deck = main



def player_turn( center_value: int, player):
    
    print ("__C'est au joueur",player.numero_joueur + 1,"de jouer__")
    print(". La valeur du centre est",center_value,".")
    w = True
    dict_deck = convert(player.deck)
    
    
    while w == True :
        print("Voici votre main")
        print(dict_deck)
        add_value = 0
        
        # Dans la boucle tour de joueur, ici on demande au joueur les cartes qu'il veut jouer
        print("Que souhaitez vous faire ?")
        print("--> 1 : Jouer des cartes ")
        print("--> 2 : Passer mon tour ")
        do = int(input(":"))
        
        if do == 1 :
            player.passed = False

            n = int(input("Combien de cartes voulez-vous jouer ? :"))
            color_list = []
            value_list = []
            count = -1
            min = 51
            
            for i in range (n):
                color = str(input("Saisir la couleur de la carte :"))
                value = int(input("Saisir la valeur de la carte :"))
                color_list.append(color) # On ajoute les couleurs de carte à une liste pour pouvoir les comparer
                value_list.append(value) # On ajoute les valeurs de carte à une liste pour pouvoir les comparer 
                
            
            if len(value_list) == 1 or color_list[0] == 'baroudeur': # Si on joue une seule carte ou une carte baroudeur
                add_value = value_list[0] #La valeur est celle du premier élément de la combinaison, puisque qu'il n'y a qu'une carte
                center_value = center_value + add_value # On ajoute la valeur de la carte à celle du centre 
                
                p = len(color_list)
                for i in range(p):
                    del_card(player,player.deck,color_list[i],value_list[i])
                w = False # On sort de la boucle puisque le joueur a joué
            
            
            elif len(value_list) != 1: # Si on a plusieur cartes 
                
                for j in value_list : # On cherche à trouver la valeur minimum présente dans la liste des valeurs
                    if j < min : # On compare toutes les valeurs des cartes entre elle 
                        min = j # On récupère à chaque fois la plus petite 
                
                
                comp = value_list[0] # Valeur pour comparer dans la liste 
                
                for k in value_list: # On compare les valeurs entre elles pour savoir si le joueur à jouer QUE des cartes de même valeur
                    if k == comp : 
                        count = count + 1
                
                
                if count == len(value_list): # Si on a bien des cartes de même valeur alors on fait le calcul de la valeur totale des cartes
                    add_value = n*10 + min
                    
                
                comp2 = color_list[0] # Valeur pour comparer la liste
                
                for k2 in color_list : # On compare les couleurs entre elles pour savoir si le joueur à jouer QUE des cartes de même couleur
                    if k2 == comp2 :
                        count = count + 1
                
                
                if count == len(color_list): # Si on a bien des cartes de même couleur alors on fait le calcul de la valeur totale des cartes
                    add_value = n*10 + min
                    
                print(add_value)
                if add_value > center_value : # Si la valleur de la combinaison est plus grande que celle du centre 
                    
                    center_value = center_value + add_value # On ajoute la valeur de la combinaison à celle du centre 
                    
                    p = len(color_list)
                    
                    for i in range(p):
                        del_card(player,player.deck,color_list[i],value_list[i])

                    
                    w = False # On sort de la boucle puisque le joueur a joué
                    
            
                else :
                    print("La combinaison n'est pas valide") # On reste dans la boucle car la combinaison n'était pas valide 

        else :
            player.passed = True
            w = False  
            
            
    return center_value


def fin_de_tour(player_list: list, player):# Dans cette fontion, on veut déterminer si les trois joueurs avant celui qui joue ont passé leur tour pour savoir si la manche s'arrête
    
    liste_joueur = []
    
    for joueurs in player_list :
        
        if joueurs != player:
            liste_joueur.append(joueurs)

    if all(joueur.passed == True for joueur in liste_joueur) == True :
        return True
    else:
        return False
    

def calcul_points(player_list: list, player, manche : int):
    joueur_restant = 0 # On initialise le compteur
    
    del(player_list[player.numero_joueur]) # On supprime le joueur qui n'a plus de carte de la liste
    
    for joueur in player_list : # On compte le nombre de joueurs qui reste
        joueur_restant = joueur_restant + 1
        
    points = joueur_restant*manche # On calcule les points
    
    player.points = player.points + points # On retourne le nombre de points

def player_order(player_list: list,starter_player):
    
    index_joueur_avant = player_list.index(starter_player)
    liste = player_list[index_joueur_avant + 1:] + player_list[:index_joueur_avant +1]
   
    return liste




def del_player(player_list: list, player):
    
    for i in range (len(player_list)):
        if player_list[i] == player :
            del(player_list[i])
            
            
def tour_de_table(player_list: list, manche, center_value):
    
    tour = True

    while tour == True :


        for joueur in player_list :
            
            if fin_de_tour(player_list,joueur) == True :
                center_value = 0
                for jr in player_list:
                    jr.passed = False
                player_list = player_order(player_list,joueur)
                tour = False
                
            if joueur.deck == []:
                calcul_points(player_list,joueur,manche)
                del_player(player_list,joueur)
            
            center_value = player_turn(center_value,joueur)
            
            
            
                
    
    return player_list,center_value
                