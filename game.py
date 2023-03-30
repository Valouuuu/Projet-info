import pygame
pygame.init()
class Game :
    def __init__(self):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Velonimo")
        
    def run(self):
        #boucle du jeu
        running = True
        while running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()