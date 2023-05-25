from mysql.connector import connect

# On créer une classe pour pouvoir gérer toutes des requêtes SQL du jeu 
class Db_Handler_Game():
    def __init__(self):
        self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo") # Connexion à la bdd
    
    # Méthode pour récuprérer la couleur d'une carte       
    def color(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_color FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
    # Méthode pour récuprérer la valeur d'une carte
    def value(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_value FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
    # Méthode pour récupérer le nom de l'image d'une carte
    def image(self, id : int):
        
        cursor = self.con.cursor()
        query = "SELECT car_image FROM Cartes WHERE car_id = %s;"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        return result
    
    # Méthode pour récupérer l'id d'une carte en ayant sa couleur et sa valeur 
    def id(self,color: str, value : int):
        cursor = self.con.cursor()
        query = "SELECT car_id FROM Cartes WHERE car_color = %s and car_value = %s;"
        cursor.execute(query, (color,value,))
        result = cursor.fetchone()
        cursor.close()
        
        return result 
        
    
# db = Db_Handler()
# print(db.image(34))
        
        




