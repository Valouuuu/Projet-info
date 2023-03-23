#accéder à la base de données
from mysql.connector import connect
bdd = connect(host="127.0.0.1", user="root", password="root",database="velonimo")

#importer la classe
from joueur import Joueur

def creer_un_compte():
    id = input("id :")
    mdp = input("mdp :")
    age = input("age :")
    joueur = Joueur(id, mdp, age)
    sql = "INSERT INTO Joueur(jou_user, jou_mdp, jou_age, jou_win, jou_lose) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (joueur.id, joueur.mdp, joueur.age, joueur.win, joueur.lose))
    bdd.commit()


#accéder et modifier bdd
# cursor = bdd.cursor()
# cursor.execute("#ce que on veux faire")

cursor = bdd.cursor()


#Ajout d'un joueur



#récupération des données

cursor.execute("SELECT jou_user, jou_mdp, jou_age, jou_win, jou_lose FROM Joueur")
resultat = cursor.fetchall()

#récupérer ensemble des lignes : resultat = cursor.fetchall()
#parcourir resultat :
for Joueur in resultat:
    id, mdp, age, win, lose = Joueur
    print(id, mdp, age, win, lose)


# mettre en commentaire : Ctrl+K+C
# enlever commentaire : Ctrl+K+U

