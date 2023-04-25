from mysql.connector import connect
bdd = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")

# # Fonction pour voir si l'identifiant se trouve déjà dans la bdd
# def not_in_bdd(user: str) -> bool:
#     cursor = bdd.cursor()
#     query = f"SELECT * FROM Compte WHERE com_user = ?;"
#     cursor.execute(query, (user,))
#     result = cursor.fetchall()
#     cursor.close()

#     return len(result) == 1

# # Fonction pour créer un compte, et donc ajouter les données dans la bdd
# def create_acc(user, mdp, age):

#     cursor = bdd.cursor()
        
#     sql = "INSERT INTO Compte(com_user, com_mdp, com_age) VALUES (%s, %s, %s);"
#     cursor.execute(sql, (user, mdp, age,))
#     bdd.commit()
#     cursor.close()


# #Fonction pour aller chercher le mot de passe correspondant à l'identifiant rentré 
# def acc_password(user: str):

#     cursor = bdd.cursor()
    
#     sql = f"SELECT com_mdp FROM Compte WHERE com_user = ?;"
#     cursor.execute(sql, (user,))
#     result = cursor.fetchall()
#     bdd.commit()
#     cursor.close()
#     return dict(result[0])["com_mdp"]


# On créer une classe pour pouvoir gérer toutes des requêtes SQL
class Db_Handler():
    def __init__(self):
        self.con = connect(host="127.0.0.1", user="root", password="root",database="Velonimo") # Connexion à la bdd

    # Méthode pour ajouter/créer un compte à la bdd
    def create_acc(self, username: str, password: str, age: str):
        cursor = self.con.cursor()
        query = f"INSERT TO Compte (com_user,com_mdp,com_age) VALUES (?,?,?);"
        cursor.execute(query,(username, password, age,))
        cursor.close

    # Méthode pour récupéré le mdp qui correspond à l'id rentré par l'utilisateur
    def password_for(self, username: str):
        cursor = self.con.cursor()
        query = f"SELECT com_mdp FROM Compte WHERE com_user = ?;"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        cursor.close()
        
        return dict(result[0])['com_mdp']
    
    # Méthode pour vérifier que l'id n'existe pas déjà dans la bdd
    def is_in_bdd(self, username: str):
        cursor = self.con.cursor()
        query = f"SELECT * FROM Compte WHERE com_user = ?;"
        cursor.execute(query, (username,))
        result = cursor.fetchall()
        cursor.close()

        return len(result) == 1