def turn(player_turn,winner, player_order):
    center = 0 #valeur du centre au début du tour
    # for p in player_list: #le gagnant de la dernière manche joue (sauf si c'est la 1ère manche le plus jeune)
    d = -1
    winner_order = []
    while len(player_order) != d: #boucle du tour
        while True: #boucle de la main
            playerking == 0
            for p in player_order: 
                if playerking != player_order[p]: #si le joueur n'est pas le king
                    if not False : #si le joueur joue
                        center = player_turn(center,p.deck)
                        playerking = player_order[p]
                else : #fin du tour
                    False
            for p in player_order: #fin du tour quand les gens n'ont plus de cartes
                if len(p.deck) == 0:
                    d += 1
                    winner_order += player_order[p]
    return winner_order