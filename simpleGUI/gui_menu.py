import PySimpleGUI as sg
import main_menu as acc

connected = False

sleep_time = 10

crea_acc_layout = [ [sg.Text('Création de compte !') , sg.Text(size=(15,1))],
          [sg.Text('Identifiant :'), sg.Input(key = '-NEW_ID-')],
          [sg.Text('Mot de passe :'), sg.Input(key = '-NEW_PW-')],
          [sg.Text('Comfiramation du mot de passe :'), sg.Input(key='-PWC-')],
          [sg.Text('Age'), sg.Input(key = '-AGE-')],
          [sg.Button('Créer mon compte', key = '-CREATE-')],
          [sg.Button('Quitter', key = '-QUIT-')]
          ]

main_layout = [ [sg.Text('Bienvenu sur le Vélonimo !') , sg.Text(size=(15,1))],
          [sg.Text('Identifiant :'), sg.Input(key = '-ID-')],
          [sg.Text('Mot de passe :'), sg.Input(key = '-PW-')],
          [sg.Button('Connexion') , sg.Button('Créer un compte', key = '-ACCOUNT-')],
          [sg.Button('Quitter', key = '-EXIT-')]

]

layout = [[sg.pin(sg.Column(main_layout, key = '-MAIN_MENU-')),
               sg.pin(sg.Column(crea_acc_layout, key='-CREATE_ACCOUNT-', visible=False))]]


window = sg.Window('Vélonimo' , layout, finalize=True, use_default_focus=False)



while True : 
    
    event , values = window.read()
    
    
    if event == sg . WIN_CLOSED or event == '-QUIT-' or event == '-EXIT-':
        break
    
    elif event == '-ACCOUNT-': # Ici on regarde pour changer de layout si l'utilisateur veut se créer un compte
        
        window['-MAIN_MENU-'].update(visible=False)
        window['-CREATE_ACCOUNT-'].update(visible=True)

    if event == '-LOGIN-':
            acc.login(values['-ID-'], values['-PW-'])
    if event == '-CREATE-':
            acc.password_check(values['-NEW_ID-'], values['-NEW_PW-'], values['-PWC-'], values['-AGE-']) 

            
            


window.close()