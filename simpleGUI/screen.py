import pygame


def scr_sz(a):
    screen_size  = pygame.display.get_desktop_sizes()
    tu = screen_size[0]
    x = tu[0]
    y = tu[1]
    if a == 'x':
        return x
    elif a == 'y':
        return y