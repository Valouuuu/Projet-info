def message_to_screen(msg, color, pos, font, screen):
    text = font.render(msg, True, color)
    screen.blit(text, pos)