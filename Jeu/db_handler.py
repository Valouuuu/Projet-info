from mysql.connector import connect

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