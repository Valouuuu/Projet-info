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
    
    run = True    
    while run == True :
        
        playerlist = pt.tour_de_table(player_list,manche)
        
        if len(player_list) == 1 :
            run = False
        
            