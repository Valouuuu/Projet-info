from db_handler import Db_Handler
import PySimpleGUI  as sg
database_handler = Db_Handler()

# Fonction pour créer un compte 
def register(username: str, password: str, age: int):
    
    if database_handler.is_in_bdd(username) == False :
        database_handler.create_acc(username, password, age)
        sg.popup("Connected")
    else:
        sg.popup("Cet utilisateur existe déjà !")

# Interface du menu connecté 
def login(username: str, password: str):

    password_db = database_handler.password_for(username)
    if password == password_db : # Ici on vérifie que le mdp enregistré correspond à celui rentré par l'utilisateur
            sg.popup("Connected")
    else :
        sg.popup("Mot de passe incorrect !")


# Fonction pour vérifier la validité du mot de passe de comfirmation
def password_check(username: str, password: str, password_check: str, age: str):
    if password == password_check :
        register(username, password, age)
    else :
        sg.popup("La confirmation de mot de passe est incorrecte !") 
              
         



