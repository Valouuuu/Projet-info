import pygame
from db_handler import Db_Handler
from def_msg_to_screen import message_to_screen
from screen import screen_size
import button
import cartes as c

pygame.init()

blue = (0, 0, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 25)


def loop(self):
    # self.connected = True 
    # while self.run:
        
    #     for event in pygame.event.get():
            
    #         if event.type == pygame.QUIT:
    #             self.run = False
    #         handle text input
            
    #         for box in input_boxes_Create_account:
    #             box.handle_event(event)
                
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
    #                 user_info[labels_Create_account[input_boxes_Create_account.index(box)]] = box.text
    #             #"retour" button reset the input box
                
    #             if retour == True:
    #                 box.text = ""

    #         for box in input_boxes_login:
    #             box.handle_event(event)
                
    #             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
    #                 user_info[labels_login[input_boxes_login.index(box)]] = box.text
    #             #"retour" button reset the input box
                
    #             if retour == True:
    #                 box.text = ""

            
    #         retour = False
                    
    #         handle button
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             self.clicked = False
                
    # self.screen.fill((255, 255, 255))       
    
    
    # if self.connected == True :
        
    #     joueur = 1
        
    #     c.afficher_mains_dos_cartes()
    #     liste_des_cartes = c.create_all_cards()
    #     decks_joueurs = c.init_decks(liste_des_cartes)
        
    #     c.afficher_deck(self.screen , decks_joueurs , joueur , 300 , f.screen_size('y')-350)
    #     deck_en_cours = decks_joueurs [ joueur -1 ]  
    pass  
            
class Event():
    def __init__(self, screen):
        self.run = True
        self.clock = pygame.time.Clock()
        self.screen = screen

        #game variables
        self.game_paused = False
        self.connected = False
        self.clicked = False

        #define fonts
        self.font = pygame.font.SysFont("arialblack", 25)

        #define colours
        self.text_col = (255, 255, 255)

        #load card images
        self.carte_1_blue = pygame.image.load('Jeu/images_cartes/card_1_blue.png').convert()
        self.carte_2_blue = pygame.image.load('Jeu/images_cartes/card_2_blue.png').convert()
        self.carte_3_blue = pygame.image.load('Jeu/images_cartes/card_3_blue.png').convert()
        self.carte_4_blue = pygame.image.load('Jeu/images_cartes/card_4_blue.png').convert()
        self.carte_5_blue = pygame.image.load('Jeu/images_cartes/card_5_blue.png').convert()
        self.carte_6_blue = pygame.image.load('Jeu/images_cartes/card_6_blue.png').convert()
        self.carte_7_blue = pygame.image.load('Jeu/images_cartes/card_7_blue.png').convert()
        self.carte_1_red = pygame.image.load('Jeu/images_cartes/card_1_red.png').convert()
        self.carte_2_red = pygame.image.load('Jeu/images_cartes/card_2_red.png').convert()
        self.carte_3_red = pygame.image.load('Jeu/images_cartes/card_3_red.png').convert()
        self.carte_4_red = pygame.image.load('Jeu/images_cartes/card_4_red.png').convert()
        self.carte_5_red = pygame.image.load('Jeu/images_cartes/card_5_red.png').convert()
        self.carte_6_red = pygame.image.load('Jeu/images_cartes/card_6_red.png').convert()
        self.carte_7_red = pygame.image.load('Jeu/images_cartes/card_7_red.png').convert()
        self.carte_1_green = pygame.image.load('Jeu/images_cartes/card_1_green.png').convert()
        self.carte_2_green = pygame.image.load('Jeu/images_cartes/card_2_green.png').convert()
        self.carte_3_green = pygame.image.load('Jeu/images_cartes/card_3_green.png').convert()
        self.carte_4_green = pygame.image.load('Jeu/images_cartes/card_4_green.png').convert()
        self.carte_5_green = pygame.image.load('Jeu/images_cartes/card_5_green.png').convert()
        self.carte_6_green = pygame.image.load('Jeu/images_cartes/card_6_green.png').convert()
        self.carte_7_green = pygame.image.load('Jeu/images_cartes/card_7_green.png').convert()
        self.carte_1_pink = pygame.image.load('Jeu/images_cartes/card_1_pink.png').convert()
        self.carte_2_pink = pygame.image.load('Jeu/images_cartes/card_2_pink.png').convert()
        self.carte_3_pink = pygame.image.load('Jeu/images_cartes/card_3_pink.png').convert()
        self.carte_4_pink = pygame.image.load('Jeu/images_cartes/card_4_pink.png').convert()
        self.carte_5_pink = pygame.image.load('Jeu/images_cartes/card_5_pink.png').convert()
        self.carte_6_pink = pygame.image.load('Jeu/images_cartes/card_6_pink.png').convert()
        self.carte_7_pink = pygame.image.load('Jeu/images_cartes/card_7_pink.png').convert()
        self.carte_1_grey = pygame.image.load('Jeu/images_cartes/card_1_grey.png').convert()
        self.carte_2_grey = pygame.image.load('Jeu/images_cartes/card_2_grey.png').convert()
        self.carte_3_grey = pygame.image.load('Jeu/images_cartes/card_3_grey.png').convert()
        self.carte_4_grey = pygame.image.load('Jeu/images_cartes/card_4_grey.png').convert()
        self.carte_5_grey = pygame.image.load('Jeu/images_cartes/card_5_grey.png').convert()
        self.carte_6_grey = pygame.image.load('Jeu/images_cartes/card_6_grey.png').convert()
        self.carte_7_grey = pygame.image.load('Jeu/images_cartes/card_7_grey.png').convert()
        self.carte_1_brown = pygame.image.load('Jeu/images_cartes/card_1_brown.png').convert()
        self.carte_2_brown = pygame.image.load('Jeu/images_cartes/card_2_brown.png').convert()
        self.carte_3_brown = pygame.image.load('Jeu/images_cartes/card_3_brown.png').convert()
        self.carte_4_brown = pygame.image.load('Jeu/images_cartes/card_4_brown.png').convert()
        self.carte_5_brown = pygame.image.load('Jeu/images_cartes/card_5_brown.png').convert()
        self.carte_6_brown = pygame.image.load('Jeu/images_cartes/card_6_brown.png').convert()
        self.carte_7_brown = pygame.image.load('Jeu/images_cartes/card_7_brown.png').convert()
        self.carte_1_yellow = pygame.image.load('Jeu/images_cartes/card_1_yellow.png').convert()
        self.carte_2_yellow = pygame.image.load('Jeu/images_cartes/card_2_yellow.png').convert()
        self.carte_3_yellow = pygame.image.load('Jeu/images_cartes/card_3_yellow.png').convert()
        self.carte_4_yellow = pygame.image.load('Jeu/images_cartes/card_4_yellow.png').convert()
        self.carte_5_yellow = pygame.image.load('Jeu/images_cartes/card_5_yellow.png').convert()
        self.carte_6_yellow = pygame.image.load('Jeu/images_cartes/card_6_yellow.png').convert()
        self.carte_7_yellow = pygame.image.load('Jeu/images_cartes/card_7_yellow.png').convert()
        self.carte_25_baroudeur = pygame.image.load('Jeu/images_cartes/card_25_baroudeur.png').convert()
        self.carte_30_baroudeur = pygame.image.load('Jeu/images_cartes/card_30_baroudeur.png').convert()
        self.carte_35_baroudeur = pygame.image.load('Jeu/images_cartes/card_35_baroudeur.png').convert()
        self.carte_40_baroudeur = pygame.image.load('Jeu/images_cartes/card_40_baroudeur.png').convert()
        self.carte_45_baroudeur = pygame.image.load('Jeu/images_cartes/card_45_baroudeur.png').convert()
        self.carte_50_baroudeur = pygame.image.load('Jeu/images_cartes/card_50_baroudeur.png').convert()

        #load button images
        self.exit_img = pygame.image.load("Menu Velonimo V2/images/button_exit.png").convert_alpha()
        self.back_img = pygame.image.load("Menu Velonimo V2/images/button_retour.png").convert_alpha()
        self.pass_img = pygame.image.load("Jeu/imgbutton/pass_button.png").convert_alpha()

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

        retour = False

        # boucle de saisie des informations
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                retour = False
                #handle button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = False
                
            self.screen.fill((255, 255, 255))  

            #Jeu
            if self.game_paused == False:
                input = True
                #create card instances
                carte_1_blue =  button.Button(screen_size('x')/2-157/2, screen_size('y')/2-100, self.carte_1_blue, 1)
                carte_2_blue = button.Button(screen_size('x')/2-187/2, screen_size('y')/2-40, self.carte_2_blue, 1)
                #card
                if carte_1_blue.draw(self.screen) and self.clicked == False:
                    self.clicked = True
                if carte_2_blue.draw(self.screen) and self.clicked == False:
                    self.clicked = True
                

            if self.game_paused == True:
                #create button instances
                Retour = button.Button(screen_size('x')/2-79/2, screen_size('y')/2+20, self.back_img, 1)

                if Retour.draw(self.screen) and self.clicked == False:
                    self.game_paused = False
                    self.clicked = True
                if self.quitter.draw(self.screen) and self.clicked == False:
                    self.run = False   # on sort du programme


            
            pygame.display.update()
            self.clock.tick(60)
            
                
            
            

            
        
        

            
            