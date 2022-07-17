# create centered and left aligned text scroller

import pygame
pygame.init()

display = pygame.display.set_mode((1280, 720))
BLACK = (0, 0, 0)
WHITE = (240, 240, 240)

# pygame font renders 

# new font object

font = pygame.font.Font('assets/fonts/yapix.ttf', 30)
text = font.render('this is a string!', False, BLACK, None)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()

    display.fill(WHITE)
    display.blit(text, (200, 400))
    pygame.display.update()