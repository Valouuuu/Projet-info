import pygame
import button

#game loop
class Game():
    def __init__(self):
        self.run = True
        self.clock = pygame.time.Clock()

        #game variables
        self.game_paused = False
        self.connected = False
        self.menu_state = "main"

        
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
        resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
        options_img = pygame.image.load("images/button_options.png").convert_alpha()
        quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
        video_img = pygame.image.load('images/button_video.png').convert_alpha()
        audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
        keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
        back_img = pygame.image.load('images/button_back.png').convert_alpha()


        creeruncompte_img = pygame.image.load("images/button_creeruncompte.png").convert_alpha()
        jaidejauncompte_img = pygame.image.load("images/button_jaidejauncompte.png").convert_alpha()

        #create button instances
        self.resume_button = button.Button(304, 125, resume_img, 1)
        self.options_button = button.Button(297, 250, options_img, 1)
        self.quit_button = button.Button(336, 375, quit_img, 1)
        self.video_button = button.Button(226, 75, video_img, 1)
        self.audio_button = button.Button(225, 200, audio_img, 1)
        self.keys_button = button.Button(246, 325, keys_img, 1)
        self.back_button = button.Button(332, 450, back_img, 1)

        self.creeruncompte = button.Button(310, 400, creeruncompte_img, 1)
        self.jaidejauncompte =  button.Button(300, 200, jaidejauncompte_img, 1)


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

            screen.fill((255, 255, 255))

            #check if the user have an account
            if self.connected == False :
                self.menu_state = "Connection"
            
            #AccountMenu
            if self.menu_state == "Connection":
                if self.creeruncompte.draw(screen):
                    self.menu_state == "Create_account"
                    print("creeruncompte")
                if self.jaidejauncompte.draw(screen):
                    self.menu_state == "login"
                    print("seconnecter")
                if Game.create_input(self, screen, self.user_text, 200, 200, 140, 32):
                    pass

            #créer un compte
            if self.menu_state == "Create_account":
                pass

            #se connecter
            if self.menu_state == "login":
                pass


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