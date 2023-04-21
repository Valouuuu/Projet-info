#accéder à la base de données
from mysql.connector import connect
bdd = connect(host="127.0.0.1", user="root", password="root",database="Velonimo")

# #importer la classe
# from Compte import Compte




# #accéder et modifier bdd
# # cursor = bdd.cursor()
# # cursor.execute("#ce que on veux faire")

# cursor = bdd.cursor()
id = input("id :")
mdp = input("mdp :")
age = input("age :")

def create_acc(id, mdp, age):
    
    cursor = bdd.cursor()
    
    sql = "INSERT INTO Compte(com_user, com_mdp, com_age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (id, mdp, age,))
    bdd.commit()

create_acc()
# #Ajout d'un joueur



# #récupération des données

# cursor.execute("SELECT com_user, com_mdp, com_age, com_win, com_lose FROM Compte")
# resultat = cursor.fetchall()

# #récupérer ensemble des lignes : resultat = cursor.fetchall()
# #parcourir resultat :
# for Compte in resultat:
#     id, mdp, age, win, lose = Compte
#     print(id, mdp, age, win, lose)


# # mettre en commentaire : Ctrl+K+C
# # enlever commentaire : Ctrl+K+U


