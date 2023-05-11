from mysql.connector import connect
import pygame
import random
from player import Joueur
import player as p


class Cartes():

    def __init__(self):
        self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")
        self.deck = []
    # Méthode pour mélanger les cartes
    def Shuffle():
        
        list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
        ,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40
        ,41,42,43,44,45,46,47,48,48,50,51,52,53,54,55]

        a = 3 # Correspond au nombre de joueurs, à récupérer avant de lancer la partie 

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

        # for p in player_list:
        #     print(p.deck)

    # Méthode pour pour récupérer la couleur d'une carte
    def color_card(self, card_id):
            
            cursor = self.con.cursor()
            query = "SELECT car_color FROM Cartes WHERE car_id = %s;"
            cursor.execute(query, (card_id,))
            result = cursor.fetchall()
            cursor.close()
            
            return result


       # Méthode pour pour récupérer la valeur d'une carte
    def value_card(self, card_id):
            
            cursor = self.con.cursor()
            query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
            cursor.execute(query, (card_id,))
            result = cursor.fetchall()
            cursor.close()
            
            return result












     # def value_card(self, deck):

    #     final_list = []
        
    #     for i in range (0,7):
    #         a = str(deck[i])
    #         cursor = self.con.cursor()
    #         query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
    #         cursor.execute(query, (a,))
    #         result = cursor.fetchall()
    #         cursor.close()
            
    #         final_list = final_list + result
        
    #     return final_list


