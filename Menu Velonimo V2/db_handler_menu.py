from mysql.connector import connect
import PySimpleGUI as sg
bdd = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")

# On créer une classe pour pouvoir gérer toutes des requêtes SQL
class Db_Handler():
    def __init__(self):
        self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo") # Connexion à la bdd

    # Méthode pour ajouter/créer un compte à la bdd
    def create_acc(self, username: str, password: str, age: str):
        cursor = self.con.cursor()
        query = "INSERT INTO Compte (com_user,com_mdp,com_age) VALUES (%s,%s,%s);"
        cursor.execute(query,(username, password, age,))
        self.con.commit()
        cursor.close

    # Méthode pour récupérer le mdp qui correspond à l'id rentré par l'utilisateur
    def password_for(self, username: str):
        cursor = self.con.cursor()
        query = "SELECT com_mdp FROM Compte WHERE com_user = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        return result[0]
    
    # Méthode pour vérifier que l'id n'existe pas déjà dans la bdd
    def is_in_bdd(self, username: str):
        cursor = self.con.cursor()
        query = "SELECT * FROM Compte WHERE com_user = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        cursor.close()

        if len(result) > 0 :
            return True
        else :
            return False
      
    # Méthode pour récupérer le nombre de victoires/défaites d'un joueur  
    def recup_win_loose(self, username : str):
        
        liste = [] #Ici on créer une liste dans laquelle on retournera [victoires , défaites]
        
        # On fait la query sql pour récuper les victoires
        cursor = self.con.cursor()
        query = "SELECT com_win FROM Compte WHERE com_user = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
       
        liste.append(result[0]) # On ajoute le résultat à la liste 
        
        # On fait la query sql pour récuper les défaites
        query = "SELECT com_lose FROM Compte WHERE com_user = %s;"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        liste.append(result[0]) # On ajoute le résultat à la liste 
        
        cursor.close()
        
        return liste 
    
    # Méthode pour ajouter une vitoire/défaite à un joueur 
    def add_win_lose(self ,username : str , wl : int):
        
        db = Db_Handler()
        
        win_lose = db.recup_win_loose('Lau') # On va chercher le nombre de victoires/défaites du joueur
            
            
            
        
        if wl == 1 : # Si c'est une victoire
            
            win_up = win_lose[0] + 1 # On ajoute 1 au nombre de victoires
            
            # Query pour mettre à jour le nombre de victroires 
            cursor = self.con.cursor()
            query = "UPDATE Compte SET com_win = %s WHERE com_user = %s;"
            cursor.execute(query,(win_up ,username))
            self.con.commit()
            cursor.close
            
        if wl == 0 :
            lose_up = win_lose[1] + 1 # On ajoute 1 au nombre de défaites
            
            # Query pour mettre à jour le nombre de défaites
            cursor = self.con.cursor()
            query = "UPDATE Compte SET com_lose = %s WHERE com_user = %s;"
            cursor.execute(query,(lose_up, username))
            self.con.commit()
            cursor.close




