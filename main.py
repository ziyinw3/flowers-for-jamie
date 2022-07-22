import pygame

from src.constants import GAME_CAPTION, GAME_ICON, SCREEN_WIDTH, SCREEN_HEIGHT
from src.states import music_on, sound_on, game_is_active, full_screen, active_scene

if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption(GAME_CAPTION)
    pygame.display.set_icon(GAME_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()    

    while game_is_active:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_is_active = False
                if event.key == pygame.K_F11:
                    if full_screen:
                        full_screen = False
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                    else:
                        full_screen = True
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)