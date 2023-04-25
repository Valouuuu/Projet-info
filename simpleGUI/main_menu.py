from db_handler import Db_Handler
import PySimpleGUI  as sg
database_handler = Db_Handler()

# Fonction pour créer un compte 
def register(username: str, password: str, age: int):
    
    if database_handler.is_in_bdd(username) == False :
        database_handler.create_acc(username, password, age)
        sg.popup("Connected")
    else:
        sg.popup("utilisateur déjà dans la bdd")

# Interface du menu connecté 
def login(username: str, password: str):

    password_db = database_handler.password_for(username)
    if password == password_db : # Ici on vérifie que le mdp enregistré correspond à celui rentré par l'utilisateur
            sg.popup("Connected")
    else :
        sg.popup("Mot de passe incorrect ")






