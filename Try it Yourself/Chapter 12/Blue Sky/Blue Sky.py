import sys
import pygame
from character import Character


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    background = (0, 0, 200)
    pygame.display.set_caption("Blue Skies")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(background)
        character = Character(screen)
        character.blitme()
        pygame.display.flip()


run_game()
