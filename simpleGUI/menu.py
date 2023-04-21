import PySimpleGUI as sg
from create_account import not_in_bdd
import datetime
#from create_account import create_acc
connected = False

sleep_time = 10

crea_acc_layout = [ [sg.Text('Création de compte !') , sg.Text(size=(15,1))],
          [sg.Text('Identifiant :'), sg.Input(key = '-ID-')],
          [sg.Text('Mot de passe :'), sg.Input(key = '-PW-')],
          [sg.Text('Comfiramation du mot de passe :'), sg.Input(key='-PWC-')],
          [sg.Button('Créer mon compte')],
          [sg.Button('Quitter')]
          ]

main_layout = [ [sg.Text('Bienvenu sur le Vélonimo !') , sg.Text(size=(15,1))],
          [sg.Text('Identifiant :'), sg.Input(key = '-ID-')],
          [sg.Text('Mot de passe :'), sg.Input(key = '-PW-')],
          [sg.Button('Connexion') , sg.Button('Créer un compte', key = '-ACCOUNT-')],
          [sg.Button('Quitter')]

]

layout = [[sg.pin(sg.Column(main_layout, key = '-MAIN_MENU-')),
               sg.pin(sg.Column(crea_acc_layout, key='-CREATE_ACCOUNT-', visible=False))]]


window = sg.Window('Vélonimo' , layout, finalize=True, use_default_focus=False)

id = window['-ID-']
pw = window['-PW-']




while True : 
    
    event , value = window.read()
    
    if event == sg . WIN_CLOSED or event == 'Quitter':
        break
    
    elif event == '-ACCOUNT-':
        
        window['-MAIN_MENU-'].update(visible=False)
        window['-CREATE_ACCOUNT-'].update(visible=True)
        
        #On souhaite regarder si le pseudo est déja dans la bdd
        #if not_in_bdd(id) is True :
            

           


window.close()