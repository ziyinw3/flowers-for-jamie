# create centered and left aligned text scroller

import pygame
pygame.init()

display = pygame.display.set_mode((1280, 720))
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)

clock = pygame.time.Clock()

# pygame font renders 

# new font object

string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
char_count = len(string)

font = pygame.font.Font('assets/fonts/basis33.ttf', 15)
text_line = font.render(string, False, BLACK).convert_alpha()
# text object: loaded in full string to be written
intermediate = text_line.copy().get_rect()
position = 0
text_position = [1280/2, 720/2]

# text_shown = pygame.Surface((intermediate.w, intermediate.h), pygame.SRCALPHA)
# text_shown_rect = text_shown.get_rect()

increment = text_line.get_rect()[2] / char_count

while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()    
    # create new surface
    intermediate = text_line.copy().get_rect()
    intermediate[2] = position
    if position + increment <= text_line.copy().get_rect()[2]:
        position += increment   
        text_position[0] -= increment / 2
    text_shown = pygame.Surface((intermediate.w, intermediate.h), pygame.SRCALPHA)

    display.fill(WHITE)
    text_shown.blit(text_line, (0,0))
    display.blit(text_shown, (text_position[0], text_position[1]))
    pygame.display.update()