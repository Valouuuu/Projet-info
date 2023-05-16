def player_turn(centervalue : int,deck : []):
    w = True
    while w == True :
        add_value = 0
        # Dans la boucle tour de joueur, ici on demande au joueur les cartes qu'il veut jouer
        print("Que souhaitez vous faire ?")
        print("1 : Jouer des cartes ")
        print("2 : Passer mon tour ")
        do = int(input(":"))
        if do == 1 :
            n = int(input("Combien de cartes voulez-vous jouer ? :"))
            while add_value < centervalue :  
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
                w = False  
        else:
            w = False

player_turn(5, [1])