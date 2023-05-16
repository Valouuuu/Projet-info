import pygame

# Méthode pour récuprer les dimensions de l'écran en x ou en y
def screen_size(size: str):
    
    screen_size  = pygame.display.get_desktop_sizes() # On récupère les dimensions de l'écran
    tu = screen_size[0] # on récupère le tuple 
    x = tu[0] # Largeur
    y = tu[1] # Hauteur
    
    if size == 'x':
        
        return x # On retourne la largeur
    
    elif size == 'y':
        
        return y # On retourne la hauteur 