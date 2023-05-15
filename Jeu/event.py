import pygame
# from inputbox import InputBox
# from db_handler import Db_Handler
# from def_msg_to_screen import message_to_screen
import fonctions as f
import cartes as c

pygame.init()

blue = (0, 0, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 25)


class Event():
    
    def __init__(self,screen):
        
        self.run = True
        self.clock = pygame.time.Clock()
        self.screen = screen

        #game variables
        self.game_paused = False
        self.connected = False
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
        
        # self.carte_1_blue = pygame.image.load('Jeu/images_cartes/card_1_blue.png').convert()
        # self.carte_2_blue = pygame.image.load('Jeu/images_cartes/card_2_blue.png').convert()
        # self.carte_3_blue = pygame.image.load('Jeu/images_cartes/card_3_blue.png').convert()
        # self.carte_4_blue = pygame.image.load('Jeu/images_cartes/card_4_blue.png').convert()
        # self.carte_5_blue = pygame.image.load('Jeu/images_cartes/card_5_blue.png').convert()
        # self.carte_6_blue = pygame.image.load('Jeu/images_cartes/card_6_blue.png').convert()
        # self.carte_7_blue = pygame.image.load('Jeu/images_cartes/card_7_blue.png').convert()
        # self.carte_1_red = pygame.image.load('Jeu/images_cartes/card_1_red.png').convert()
        # self.carte_2_red = pygame.image.load('Jeu/images_cartes/card_2_red.png').convert()
        # self.carte_3_red = pygame.image.load('Jeu/images_cartes/card_3_red.png').convert()
        # self.carte_4_red = pygame.image.load('Jeu/images_cartes/card_4_red.png').convert()
        # self.carte_5_red = pygame.image.load('Jeu/images_cartes/card_5_red.png').convert()
        # self.carte_6_red = pygame.image.load('Jeu/images_cartes/card_6_red.png').convert()
        # self.carte_7_red = pygame.image.load('Jeu/images_cartes/card_7_red.png').convert()
        # self.carte_1_green = pygame.image.load('Jeu/images_cartes/card_1_green.png').convert()
        # self.carte_2_green = pygame.image.load('Jeu/images_cartes/card_2_green.png').convert()
        # self.carte_3_green = pygame.image.load('Jeu/images_cartes/card_3_green.png').convert()
        # self.carte_4_green = pygame.image.load('Jeu/images_cartes/card_4_green.png').convert()
        # self.carte_5_green = pygame.image.load('Jeu/images_cartes/card_5_green.png').convert()
        # self.carte_6_green = pygame.image.load('Jeu/images_cartes/card_6_green.png').convert()
        # self.carte_7_green = pygame.image.load('Jeu/images_cartes/card_7_green.png').convert()
        # self.carte_1_pink = pygame.image.load('Jeu/images_cartes/card_1_pink.png').convert()
        # self.carte_2_pink = pygame.image.load('Jeu/images_cartes/card_2_pink.png').convert()
        # self.carte_3_pink = pygame.image.load('Jeu/images_cartes/card_3_pink.png').convert()
        # self.carte_4_pink = pygame.image.load('Jeu/images_cartes/card_4_pink.png').convert()
        # self.carte_5_pink = pygame.image.load('Jeu/images_cartes/card_5_pink.png').convert()
        # self.carte_6_pink = pygame.image.load('Jeu/images_cartes/card_6_pink.png').convert()
        # self.carte_7_pink = pygame.image.load('Jeu/images_cartes/card_7_pink.png').convert()
        # self.carte_1_grey = pygame.image.load('Jeu/images_cartes/card_1_grey.png').convert()
        # self.carte_2_grey = pygame.image.load('Jeu/images_cartes/card_2_grey.png').convert()
        # self.carte_3_grey = pygame.image.load('Jeu/images_cartes/card_3_grey.png').convert()
        # self.carte_4_grey = pygame.image.load('Jeu/images_cartes/card_4_grey.png').convert()
        # self.carte_5_grey = pygame.image.load('Jeu/images_cartes/card_5_grey.png').convert()
        # self.carte_6_grey = pygame.image.load('Jeu/images_cartes/card_6_grey.png').convert()
        # self.carte_7_grey = pygame.image.load('Jeu/images_cartes/card_7_grey.png').convert()
        # self.carte_1_brown = pygame.image.load('Jeu/images_cartes/card_1_brown.png').convert()
        # self.carte_2_brown = pygame.image.load('Jeu/images_cartes/card_2_brown.png').convert()
        # self.carte_3_brown = pygame.image.load('Jeu/images_cartes/card_3_brown.png').convert()
        # self.carte_4_brown = pygame.image.load('Jeu/images_cartes/card_4_brown.png').convert()
        # self.carte_5_brown = pygame.image.load('Jeu/images_cartes/card_5_brown.png').convert()
        # self.carte_6_brown = pygame.image.load('Jeu/images_cartes/card_6_brown.png').convert()
        # self.carte_7_brown = pygame.image.load('Jeu/images_cartes/card_7_brown.png').convert()
        # self.carte_1_yellow = pygame.image.load('Jeu/images_cartes/card_1_yellow.png').convert()
        # self.carte_2_yellow = pygame.image.load('Jeu/images_cartes/card_2_yellow.png').convert()
        # self.carte_3_yellow = pygame.image.load('Jeu/images_cartes/card_3_yellow.png').convert()
        # self.carte_4_yellow = pygame.image.load('Jeu/images_cartes/card_4_yellow.png').convert()
        # self.carte_5_yellow = pygame.image.load('Jeu/images_cartes/card_5_yellow.png').convert()
        # self.carte_6_yellow = pygame.image.load('Jeu/images_cartes/card_6_yellow.png').convert()
        # self.carte_7_yellow = pygame.image.load('Jeu/images_cartes/card_7_yellow.png').convert()
        # self.carte_25_baroudeur = pygame.image.load('Jeu/images_cartes/card_25_baroudeur.png').convert()
        # self.carte_30_baroudeur = pygame.image.load('Jeu/images_cartes/card_30_baroudeur.png').convert()
        # self.carte_35_baroudeur = pygame.image.load('Jeu/images_cartes/card_35_baroudeur.png').convert()
        # self.carte_40_baroudeur = pygame.image.load('Jeu/images_cartes/card_40_baroudeur.png').convert()
        # self.carte_45_baroudeur = pygame.image.load('Jeu/images_cartes/card_45_baroudeur.png').convert()
        # self.carte_50_baroudeur = pygame.image.load('Jeu/images_cartes/card_50_baroudeur.png').convert()
        
        # Boutons 
        self.exit_img = pygame.image.load("Menu Velonimo V2/images/button_exit.png").convert_alpha()
        self.play_img = pygame.image.load("Menu Velonimo V2/images/button_jouer.png").convert_alpha()
        
    def loop(self):
        self.connected = True 
        while self.run:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.run = False
                #handle text input
                
                # for box in input_boxes_Create_account:
                #     box.handle_event(event)
                    
                #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #         user_info[labels_Create_account[input_boxes_Create_account.index(box)]] = box.text
                #     #"retour" button reset the input box
                    
                #     if retour == True:
                #         box.text = ""

                # for box in input_boxes_login:
                #     box.handle_event(event)
                    
                #     if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                #         user_info[labels_login[input_boxes_login.index(box)]] = box.text
                #     #"retour" button reset the input box
                    
                #     if retour == True:
                #         box.text = ""

                
                # retour = False
                        
                #handle button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = False
                    
        self.screen.fill((255, 255, 255))       
        
        
        if self.connected == True :
            
            joueur = 1
            
            c.afficher_mains_dos_cartes(self.screen)
            liste_des_cartes = c.create_all_cards()
            decks_joueurs = c.init_decks(liste_des_cartes)
            
            c.afficher_deck(self.screen , decks_joueurs , joueur , 300 , f.screen_size('y')-350)
            deck_en_cours = decks_joueurs [ joueur -1 ]
            
            
            
            