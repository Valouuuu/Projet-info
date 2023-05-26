import player_turn as pt
import player 
from db_handler_game import Db_Handler_Game
Db = Db_Handler_Game()

points = 0
center_value = 0
player_list = player.deckplayer(4)

for manche in range (5):
    
    run = True    
    while run == True :
        
        playerlist,center_value = pt.tour_de_table(player_list,manche,center_value)
        
        if len(player_list) == 1 :
            run = False
            
for joueurs in player_list :
    
    if joueurs.points > points :
        winner = joueurs
        
print("Le gagnant est le joueur",winner.numero_joueur + 1)
        
        
    
        
            