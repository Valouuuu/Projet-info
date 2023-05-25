from manche_akiletour import Joueur
joueur = Joueur()

def main(playeralive,player_order, player_turn,winner):
    loop = True
    firsturn = True
    while loop == True: #boucle de la main
        for p in playeralive: 
            if player_order[winner] != player_order[p] and firsturn == False: #si le joueur n'est pas le king (dernière personne à avoir mis une carte au centre)
                    result = player_turn(center,p.deck)
                    if result != False : #verif si le joueur passe son tour ou joue
                        center = result
                        winner = player_order[p]

            else : #fin du tour
                loop == False
                return winner
                
                
                
                
def turn(player_turn,winner, player_order):
    center = 0 #valeur du centre au début du tour
    # for p in player_list: #le gagnant de la dernière manche joue (sauf si c'est la 1ère manche le plus jeune)
    winner_order = []
    playeralive = player_order
    while len(playeralive) != 1: #boucle du tour
        for p in playeralive :
            if playeralive[p].joueur.deck == []:
                winner_order += playeralive[p]
                del playeralive[p]

        winner = main(playeralive,player_order,player_turn,winner) #boucle de la main
        firsturn = False
    return winner_order