import pygame
from inputbox import InputBox
from db_handler import Db_Handler
from def_msg_to_screen import message_to_screen
from screen import screen_size
import button

database_handler = Db_Handler()

#for the rules
import webbrowser

pygame.init()


# import verif

# définition des couleurs utilisées
blue = (0, 0, 255)
black = (0, 0, 0)

# définition des polices utilisées
font = pygame.font.SysFont(None, 25)

class Game():
    def __init__(self, screen):
        self.run = True
        self.clock = pygame.time.Clock()
        self.screen = screen

        #game variables
        self.game_paused = False
        self.connected = False
        self.menu_state = "Connection"
        self.clicked = False

        
        # #parametre pour input
        self.user_text = ''
        self.base_front = pygame.font.Font(None, 32)
        self.color_active = pygame.Color('Blue')
        self.color_passive = pygame.Color('Gray')
        self.color = self.color_passive
        self.active = False


        #define fonts
        self.font = pygame.font.SysFont("arialblack", 25)

        #define colours
        self.text_col = (255, 255, 255)

        #load button images
        self.creeruncompte_img = pygame.image.load("Menu Velonimo V2/images/button_creeruncompte.png").convert_alpha()
        self.jaidejauncompte_img = pygame.image.load("Menu Velonimo V2/images/button_jaidejauncompte.png").convert_alpha()
        self.exit_img = pygame.image.load("Menu Velonimo V2/images/button_exit.png").convert_alpha()
        self.icon_img = pygame.image.load("Menu Velonimo V2/images/ImageMenu.jpg").convert_alpha()
        self.settings_img = pygame.image.load("Menu Velonimo V2/images/button_paramètres.png").convert_alpha()
        self.play_img = pygame.image.load("Menu Velonimo V2/images/button_jouer.png").convert_alpha()
        self.stats_img = pygame.image.load("Menu Velonimo V2/images/button_stats.png").convert_alpha()
        self.rules_img = pygame.image.load("Menu Velonimo V2/images/button_regles.png").convert_alpha()
        self.back_img = pygame.image.load("Menu Velonimo V2/images/button_retour.png").convert_alpha()
        self.valider_img = pygame.image.load("Menu Velonimo V2/images/button_valider.png").convert_alpha()

        #load error
        self.error_img = pygame.image.load("Menu Velonimo V2/images/error.png").convert_alpha()

        #load img
        self.title = pygame.image.load("Menu Velonimo V2/images/titre.png").convert_alpha()
        self.animal = pygame.image.load("Menu Velonimo V2/images/animaux.jpg").convert_alpha()

        #changement de l'icone de la fenêtre
        pygame.display.set_icon(self.icon_img)
        
        #create button instances
        self.quitter =  button.Button(screen_size('x')/2-54/2, screen_size('y')/2+20, self.exit_img, 1)
        
    def draw_title(text, self, text_col, x, y):
        img = self.font.render(text, True, text_col)
        width = img.get_width()
        self.screen.blit(img, (x - (width / 2), y))

    def draw_text(text, self, text_col, x, y):
        img = self.font.render(text, True, text_col)
        width = img.get_width()
        self.screen.blit(img, (x , y))

    def create_input(self, text, x, y, width, height):
        self.input_rect = pygame.Rect(x, y, width, height)
        text_surface = self.base_front.render(text, True, (0, 0, 0))
        self.input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.draw.rect(self.screen, self.color, self.input_rect, 2)
        self.screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

    def loop(self) :
        user_info = {}

        # définition des champs de saisie
        input_boxes_Create_account = [
            InputBox(screen_size('x')/2-100, screen_size('y')/2-200, 140, 32),
            InputBox(screen_size('x')/2-100, screen_size('y')/2-120, 140, 32),
            InputBox(screen_size('x')/2-100, screen_size('y')/2-40, 140, 32)
        ]
        input_boxes_login = [
            InputBox(screen_size('x')/2-100, screen_size('y')/2-120, 140, 32),
            InputBox(screen_size('x')/2-100, screen_size('y')/2-40, 140, 32)
        ]
        # définition des libellés pour chaque champ de saisie
        labels_Create_account = ['', '', '']
        labels_login = ['', '']

        retour = False

        # boucle de saisie des informations
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                #handle text input
                for box in input_boxes_Create_account:
                    box.handle_event(event)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        user_info[labels_Create_account[input_boxes_Create_account.index(box)]] = box.text
                    #"retour" button reset the input box
                    if retour == True:
                        box.text = ""

                for box in input_boxes_login:
                    box.handle_event(event)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        user_info[labels_login[input_boxes_login.index(box)]] = box.text
                    #"retour" button reset the input box
                    if retour == True:
                        box.text = ""

                
                retour = False
                        
                #handle button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = False
            
            
            self.screen.fill((255, 255, 255))  

            #AccountMenu
            if self.menu_state == "Connection":
                input = True

                #create button instances
                jaidejauncompte =  button.Button(screen_size('x')/2-157/2, screen_size('y')/2-100, self.jaidejauncompte_img, 1)
                creeruncompte = button.Button(screen_size('x')/2-187/2, screen_size('y')/2-40, self.creeruncompte_img, 1)

                #create background
                self.screen.blit(self.title, (screen_size('x')/2-325, screen_size('y')/2-350))
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

                #button
                if creeruncompte.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Create_account"
                    self.clicked = True
                if jaidejauncompte.draw(self.screen) and self.clicked == False:
                    self.menu_state = "login"
                    self.clicked = True
                if self.quitter.draw(self.screen) and self.clicked == False:
                    self.run = False   # on sort du programme

            #créer un compte
            if self.menu_state == "Create_account":
                #create button instances
                Retour = button.Button(screen_size('x')/2-79/2+50, screen_size('y')/2+20, self.back_img, 1)
                valider = button.Button(screen_size('x')/2-81/2-50, screen_size('y')/2+20, self.valider_img, 1)
                
                #notif erreur
                error = button.Button(screen_size('x')/2-150/2-50, screen_size('y')/2+20, self.error_img, 1)

                #create background
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

                #text
                Game.draw_title("Veuillez renseigner :", self, "Black", screen_size('x')/2, screen_size('y')/2-300)
                Game.draw_text("identifiant :", self, "Black", screen_size('x')/2-100, screen_size('y')/2-240)
                Game.draw_text("mot de passe :", self, "Black", screen_size('x')/2-100, screen_size('y')/2-160)
                Game.draw_text("age :",self, "Black", screen_size('x')/2-100, screen_size('y')/2-80)

                #input
                for i, box in enumerate(input_boxes_Create_account):
                    box.draw(self.screen, font)
                    message_to_screen(labels_Create_account[i], black, (box.rect.x - 75, box.rect.y + 5), font, self.screen)

                #button
                if Retour.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Connection"
                    self.clicked = True
                    retour = True

                if valider.draw(self.screen) and self.clicked == False :
                    #on récupère le texte de chaque input
                    id = ['','','']
                    k = 0
                    for box in input_boxes_Create_account:
                        id[k] = box.text
                        k += 1

                    #on créé le compte (+ vérification si déjà créé ou si cases vides)
                    if database_handler.is_in_bdd(id[0]) == False and id[0] and id[1] and id[2] and int(id[2]):
                        database_handler.create_acc(id[0], id[1], int(id[2]))
                        self.menu_state = "Connected"
                    else:
                        error.draw(self.screen)

            #se connecter
            if self.menu_state == "login":
                #create button instances
                Retour = button.Button(screen_size('x')/2-79/2+50, screen_size('y')/2+20, self.back_img, 1)
                valider = button.Button(screen_size('x')/2-81/2-50, screen_size('y')/2+20, self.valider_img, 1)

                #notif erreur
                error = button.Button(screen_size('x')/2-150/2-50, screen_size('y')/2+20, self.error_img, 1)
                
                #create background
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

                #text
                Game.draw_title("Veuillez rentrer :", self, "Black", screen_size('x')/2, screen_size('y')/2-220)
                Game.draw_text("Identifiant", self, "Black", screen_size('x')/2-100, screen_size('y')/2-160)
                Game.draw_text("mot de passe",self, "Black", screen_size('x')/2-100, screen_size('y')/2-80)

                #input
                for i, box in enumerate(input_boxes_login):
                    box.draw(self.screen, font)
                    message_to_screen(labels_login[i], black, (box.rect.x - 75, box.rect.y + 5), font, self.screen)      
        
                #button
                if Retour.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Connection"
                    self.clicked = True
                    retour = True
                if valider.draw(self.screen) and self.clicked == False:

                    #on récupère le texte de chaque input
                    id = ['','']
                    k = 0
                    for box in input_boxes_login:
                        id[k] = box.text
                        k += 1

                    #on vérifie les informations (+ vérif si cases vides)
                    if database_handler.is_in_bdd(id[0]) and id[0] and id[1] and id[1] == database_handler.password_for(id[0]): # Ici on vérifie que le mdp enregistré correspond à celui rentré par l'utilisateur
                        self.menu_state = "Connected"
                    else :
                        error.draw(self.screen)


            if self.menu_state == "Connected":
                #create button instances
                Jouer =  button.Button(screen_size('x')/2-96/2, screen_size('y')/2-160, self.play_img, 1)
                # Paramètres = button.Button(screen_size('x')/2-147/2, screen_size('y')/2-160, self.settings_img, 1)
                Regles = button.Button(screen_size('x')/2-105/2, screen_size('y')/2-100, self.rules_img, 1)
                Statistiques = button.Button(screen_size('x')/2-119/2, screen_size('y')/2-40, self.stats_img, 1)

                #create background
                self.screen.blit(self.title, (screen_size('x')/2-325, screen_size('y')/2-350))
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))
                
                #create button
                if Jouer.draw(self.screen) and self.clicked == False:
                    self.menu_state = "play"
                    self.clicked = True
                # if Paramètres.draw(screen) and self.clicked == False:
                #     self.menu_state = "settings"
                #     self.clicked = True
                if Regles.draw(self.screen) and self.clicked == False:
                    webbrowser.open('https://www.gazette-capitainemeeple.fr/wp-content/uploads/2021/06/velonimo-regles.pdf')
                if Statistiques.draw(self.screen) and self.clicked == False:
                    self.menu_state = "stats"
                    self.clicked = True
                if self.quitter.draw(self.screen) and self.clicked == False:
                    self.run = False   # on sort du programme

            if self.menu_state == "play":
                #create button instances
                Retour = button.Button(screen_size('x')/2-79/2+50, screen_size('y')/2+20, self.back_img, 1)
                
                if Retour.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Connected"
                    self.clicked = True
                    retour = True

            if self.menu_state == "stats": #pas fini, il faut rajouter l'interaction avec la bdd
                #create background
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

                win_lose = database_handler.recup_win_loose(id[0])
                win = win_lose[0]
                lose = win_lose[1]
                
                Retour = button.Button(screen_size('x')/2-79/2, screen_size('y')/2+20, self.back_img, 1)
                Game.draw_title("Victoires :", self, "Black", screen_size('x')/2, screen_size('y')/2-220)
                Game.draw_title(str(win), self, "Black", screen_size('x')/2, screen_size('y')/2-160)
                Game.draw_title("Défaites :", self, "Black", screen_size('x')/2, screen_size('y')/2-100)
                Game.draw_title(str(lose), self, "Black", screen_size('x')/2, screen_size('y')/2-40)
                if Retour.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Connected"
                    self.clicked = True


                
            #     # vérifie si l'utilisateur a appuyé sur la touche "Entrée" et imprime les valeurs de user_info
            #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            #         for key, value in user_info.items():
            #             print(key, ":", value)

            pygame.display.update()
            self.clock.tick(60)