import pygame
from def_msg_to_screen import message_to_screen


# classe pour les champs de saisie
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('Gray')
        self.text = text
        self.font = pygame.font.SysFont(None, 25)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (0, 0, 255) if self.active else pygame.Color('Gray')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        message_to_screen(self.text, (0, 0, 0), (self.rect.x + 5, self.rect.y + 5), font, screen)