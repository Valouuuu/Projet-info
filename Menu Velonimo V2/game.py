import pygame
import button
import webbrowser
import verif

# from screen import scr_sz

def screen_size(size):
    screen_size  = pygame.display.get_desktop_sizes()
    tu = screen_size[0]
    x = tu[0]
    y = tu[1]
    if size == 'x':
        return x
    elif size == 'y':
        return y


#game loop
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
        while self.run:
            input = False
            self.screen.fill((255, 255, 255))
            
            #AccountMenu
            if self.menu_state == "Connection":
                #create button instances
                jaidejauncompte =  button.Button(screen_size('x')/2-157/2, screen_size('y')/2-100, self.jaidejauncompte_img, 1)
                creeruncompte = button.Button(screen_size('x')/2-187/2, screen_size('y')/2-40, self.creeruncompte_img, 1)

                #create background
                self.screen.blit(self.title, (screen_size('x')/2-325, screen_size('y')/2-350))
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

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
                jaidejauncompte =  button.Button(screen_size('x')/2-157/2+100, screen_size('y')/2+20, self.jaidejauncompte_img, 1)
                valider = button.Button(screen_size('x')/2-81/2-100, screen_size('y')/2+20, self.valider_img, 1)

                input = True #trouver comment ne pas avoir à utiliser ça
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))
                Game.draw_title("Veuillez renseigner :", self, "Black", screen_size('x')/2, screen_size('y')/2-300)
                Game.draw_text("identifiant :", self, "Black", screen_size('x')/2-100, screen_size('y')/2-240)
                Game.create_input(self, self.user_text, screen_size('x')/2-100, screen_size('y')/2-200, 140, 32)
                id = self.user_text
                Game.draw_text("mot de passe :", self, "Black", screen_size('x')/2-100, screen_size('y')/2-160)
                Game.create_input(self, self.user_text, screen_size('x')/2-100, screen_size('y')/2-120, 140, 32)
                mdp = self.user_text
                Game.draw_text("age :",self, "Black", screen_size('x')/2-100, screen_size('y')/2-80)
                Game.create_input(self, self.user_text, screen_size('x')/2-100, screen_size('y')/2-40, 140, 32)
                age = self.user_text
                if jaidejauncompte.draw(self.screen) and self.clicked == False:
                    self.menu_state = "login"
                    self.clicked = True
                if valider.draw(self.screen) and self.clicked == False and id and mdp and age :
                    #code récupération info et verif database 

                    if verif.register(id, mdp, age) == True :
                        self.menu_state = "Connected"
                    else :
                        pass

                    #passage direct (temporaire) au menu
                    # self.menu_state = "Connected"
                    pass
                else :
                    pass #mettre msg erreur

            #se connecter
            if self.menu_state == "login":
                #create button instances
                creeruncompte = button.Button(screen_size('x')/2-187/2+100, screen_size('y')/2+20, self.creeruncompte_img, 1)
                valider = button.Button(screen_size('x')/2-81/2-100, screen_size('y')/2+20, self.valider_img, 1)

                input = True
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))
                Game.draw_title("Veuillez rentrer :", self, "Black", screen_size('x')/2, screen_size('y')/2-220)
                Game.draw_text("Identifiant", self, "Black", screen_size('x')/2-100, screen_size('y')/2-160)
                Game.create_input(self, self.user_text, screen_size('x')/2-100, screen_size('y')/2-120, 140, 32)
                id = self.user_text
                Game.draw_text("mot de passe",self, "Black", screen_size('x')/2-100, screen_size('y')/2-80)
                Game.create_input(self, self.user_text, screen_size('x')/2-100, screen_size('y')/2-40, 140, 32)
                mdp = self.user_text
                if creeruncompte.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Create_account"
                    self.clicked = True
                if valider.draw(self.screen) and self.clicked == False:
                    #code récupération info et verif database 
                    #passage direct (temporaire) au menu
                    self.menu_state = "Connected"

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
                pass

            if self.menu_state == "stats": #pas fini, il faut rajouter l'interaction avec la bdd
                #create background
                self.screen.blit(self.animal, (screen_size('x')/2-540, screen_size('y')-350))

                Retour = button.Button(screen_size('x')/2-79/2, screen_size('y')/2+20, self.back_img, 1)
                Game.draw_title("Victoires :", self, "Black", screen_size('x')/2, screen_size('y')/2-220)
                Game.draw_title("nbrevictoiresici", self, "Black", screen_size('x')/2, screen_size('y')/2-160)
                Game.draw_title("Défaites :", self, "Black", screen_size('x')/2, screen_size('y')/2-100)
                Game.draw_title("nbredéfaitesici", self, "Black", screen_size('x')/2, screen_size('y')/2-40)
                if Retour.draw(self.screen) and self.clicked == False:
                    self.menu_state = "Connected"
                    self.clicked = True


            #event handler                                     
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input == True:
                        if self.input_rect.collidepoint(event.pos):
                            self.active = True
                        else :
                            self.active = False
                    self.clicked = False
                #handle text input
                if event.type == pygame.TEXTINPUT:
                    if self.active == True:
                        self.user_text += event.text
                #handle special keys
                if event.type == pygame.KEYDOWN:
                    if self.active == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                if event.type == pygame.QUIT:
                    self.run = False

            if self.active :
                self.color = self.color_active
            else :
                self.color = self.color_passive
                    

            pygame.display.update()
            self.clock.tick(60)