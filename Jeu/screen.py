import pygame

def screen_size(size):
    screen_size  = pygame.display.get_desktop_sizes()
    tu = screen_size[0]
    x = tu[0]
    y = tu[1]
    if size == 'x':
        return x
    elif size == 'y':
        return y