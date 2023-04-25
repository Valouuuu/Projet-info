from db_handler import Db_Handler
import PySimpleGUI  as sg
database_handler = Db_Handler()

# Fonction pour créer un compte 
def register(username: str, password: str, age: int):
    
    database_handler.create_acc(username, password, age)
    menu_connected()

# Interface du menu connecté 
def login(username: str, password: str):

    password_db = database_handler.password_for(username)
    if database_handler.is_in_bdd(username) and  password == password_db : # Ici on vérifie que le mdp enregistré correspond à celui rentré par l'utilisateur
        menu_connected()
    else:
        print('pas correct')

# Fonction pour se connecter
def menu_connected(event):
    while True:
        if event == sg . WIN_CLOSED or event == 'Quitter' :
           break


# Interface de connexion
def menu_not_connected(event, username: str, password: str, age: int):
    while True :
        if event == '-LOGIN-':
            login(username, password)
        if event == '-CREATE-':
            register(username, password, age)


