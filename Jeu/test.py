import player_turn as pt
import player 
from db_handler_game import Db_Handler_Game
Db = Db_Handler_Game()

player_list = player.deckplayer(4)




# pt.player_turn(0,player_list[0])

# center_value = 0

# for joueur in player_list:    
#     center_value = pt.player_turn(center_value ,joueur)
#     if pt.fin_de_tour(player_list,joueur) == True :
#         center_value = 0
#         player_start = joueur.numero_joueur
#         break

for manche in range (5):
    
    center_value = 0
    tour = True
    
    while tour == True :
        reset = False
    
        for joueur in player_list :
            
            if pt.fin_de_tour(player_list,joueur) == True :
                reset = True 
                center_value = 0
                player_list = pt.player_order(player_list,joueur)
                
            if reset != True :
                center_value = pt.player_turn(center_value,joueur)
                
                if joueur.deck == []:
                    pt.calcul_points(player_list,joueur,manche)
                    pt.del_player(player_list,joueur)

        if len(player_list) == 1 :
            print("C'est la fin de la manche",manche)
            tour = False