import pygame
import button
from screen import scr_sz
#game loop
class Game():
    def __init__(self):
        self.run = True
        self.clock = pygame.time.Clock()

        #game variables
        self.game_paused = False
        self.connected = False
        self.menu_state = "Connection"

        
        # #parametre pour input
        self.user_text = ''
        self.base_front = pygame.font.Font(None, 32)
        self.color_active = pygame.Color('Blue')
        self.color_passive = pygame.Color('Gray')
        self.color = self.color_passive
        self.active = False


        #define fonts
        self.font = pygame.font.SysFont("arialblack", 40)

        #define colours
        self.text_col = (255, 255, 255)

        #load button images
        creeruncompte_img = pygame.image.load("Menu Velonimo V2/images/button_creeruncompte.png").convert_alpha()
        jaidejauncompte_img = pygame.image.load("Menu Velonimo V2/images/button_jaidejauncompte.png").convert_alpha()
        exit_img = pygame.image.load("Menu Velonimo V2/images/button_exit.png").convert_alpha()
        icon_img = pygame.image.load("Menu Velonimo V2/images/ImageMenu.jpg").convert_alpha()

        #load img
        self.title = pygame.image.load("Menu Velonimo V2/images/titre.png").convert_alpha()
        self.animal = pygame.image.load("Menu Velonimo V2/images/animaux.jpg").convert_alpha()

        #changement de l'icone de la fenêtre
        pygame.display.set_icon(icon_img)
        
        #create button instances
        self.jaidejauncompte =  button.Button(scr_sz('x')/2-100, scr_sz('y')/2-100, jaidejauncompte_img, 1)
        self.creeruncompte = button.Button(scr_sz('x')/2-115, scr_sz('y')/2-40, creeruncompte_img, 1)
        self.quitter =  button.Button(scr_sz('x')/2-50, scr_sz('y')/2+20, exit_img, 1)

        
    def draw_text(self, screen, text, x, y):
        img = self.font.render(text, True, self.text_col)
        screen.blit(img, (x, y))

    def create_input(self, screen, user_text, left, top, width, height):
        self.input_rect = pygame.Rect(left, top, width, height)
        text_surface = self.base_front.render(user_text, True, (0, 0, 0))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        screen.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))

        


    def loop(self, screen) :
        while self.run:
            input = False
            screen.fill((255, 255, 255))
            Game.draw_text(self, screen, "Press SPACE to pause", 160, 250)
            
            

            # #check if the user have an account
            # if self.connected == False :
            #     self.menu_state = "Connection"
            
            #AccountMenu
            if self.menu_state == "Connection":
                screen.blit(self.title, (scr_sz('x')/2-325, scr_sz('y')/2-350))
                screen.blit(self.animal, (scr_sz('x')/2-540, scr_sz('y')-350))
                if self.creeruncompte.draw(screen):
                    self.menu_state = "Create_account"
                if self.jaidejauncompte.draw(screen):
                    self.menu_state = "login"
                if self.quitter.draw(screen):
                    self.run = False   # on sort du programme

            #créer un compte
            if self.menu_state == "Create_account":
                input = True #trouver comment ne pas avoir à utiliser ça #draw_text not working for some reasons
                screen.blit(self.animal, (scr_sz('x')/2-540, scr_sz('y')-350))
                Game.draw_text(self, screen, "Veuillez renseigner :", 160, 250)
                Game.draw_text(self, screen, "Identifiant", 160, 300)
                Game.create_input(self, screen, self.user_text, 200, 200, 140, 32)
                Game.draw_text(self, screen, "mot de passe", 160, 350)
                Game.create_input(self, screen, self.user_text, 200, 200, 140, 32)
                Game.draw_text(self, screen, "age", 160, 400)
                Game.create_input(self, screen, self.user_text, 200, 200, 140, 32)
                if self.jaidejauncompte.draw(screen):
                    self.menu_state = "login"

            #se connecter
            if self.menu_state == "login":
                input = True
                screen.blit(self.animal, (scr_sz('x')/2-540, scr_sz('y')-350))
                Game.draw_text(self, screen, "Veuillez rentrer :", 160, 250)
                Game.draw_text(self, screen, "Identifiant", 160, 250)
                Game.create_input(self, screen, self.user_text, 200, 200, 140, 32)
                Game.draw_text(self, screen, "mot de passe", 160, 250)
                Game.create_input(self, screen, self.user_text, 200, 200, 140, 32)
                if self.creeruncompte.draw(screen):
                    self.menu_state = "Create_account"
            


            #check if game is paused  #exemples de choses que l'on peut faire
            # if self.game_paused == True:
            #     #check menu state
            #     if self.menu_state == "main":
            #     #draw pause screen buttons
            #         if self.resume_button.draw(screen):
            #             self.game_paused = False
            #         if self.options_button.draw(screen):
            #             self.menu_state = "options"
            #         if self.quit_button.draw(screen):
            #             self.run = False
            #         #check if the options menu is open
            #     if self.menu_state == "options":
            #     #draw the different options buttons
            #         if self.video_button.draw(screen):
            #             print("Video Settings")
            #         if self.audio_button.draw(screen):
            #             print("Audio Settings")
            #         if self.keys_button.draw(screen):
            #             print("Change Key Bindings")
            #         if self.back_button.draw(screen):
            #             self.menu_state = "main"
            # else:
            #     Game.draw_text(self, screen, "Press SPACE to pause", 160, 250)

            #event handler                                     
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input == True:
                        if self.input_rect.collidepoint(event.pos):
                            self.active = True
                        else :
                            self.active = False
                if event.type == pygame.KEYDOWN:
                    if self.active == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text += event.unicode
                    # if event.key == pygame.K_SPACE:
                    #     self.game_paused = True
                if event.type == pygame.QUIT:
                    self.run = False

            # Game.create_input(self, screen, 200, 200, 140, 32)

            if self.active :
                self.color = self.color_active
            else :
                self.color = self.color_passive
                    
            




            pygame.display.update()
            self.clock.tick(60)
        




#close game window
pygame.quit()