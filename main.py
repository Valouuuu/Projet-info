#accéder à la base de données
from mysql.connector import connect
bdd = connect(host="root", user="root", password="root",database="Velonimo")

#importer la classe
from joueur import Joueur


id = input("id :")
mdp = input("mdp :")
age = input("age :")
joueur = Joueur(id, mdp, age)


#accéder et modifier bdd
# cursor = bdd.cursor()
# cursor.execute("#ce que on veux faire")
cursor = bdd.cursor()


#Ajout d'un joueur

sql = "INSERT INTO Joueur(jou_user, jou_mdp, jou_age, jou_win, jou_lose) VALUES (%s, %s, %s, %s, %s)"
cursor.execute(sql, (joueur.id, joueur.mdp, joueur.age, joueur.win, joueur.lose))




#récupérer ensemble des lignes : resultat = cursor.fetchall()
#parcourir resultat :
# for Joueur in resultat:
#     id, mdp = Joueur
#     print(id, mdp)


# mettre en commentaire : Ctrl+K+C
# enlever commentaire : Ctrl+K+U

