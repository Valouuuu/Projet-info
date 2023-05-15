from mysql.connector import connect
import PySimpleGUI as sg
bdd = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")

# On créer une classe pour pouvoir gérer toutes des requêtes SQL
class Db_Handler():
    def __init__(self):
        self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo") # Connexion à la bdd
            
    def color(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_color FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
    def value(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
    def image(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_image FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
db = Db_Handler()
print(db.image(34))
        
        




