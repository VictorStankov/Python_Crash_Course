import sys
import pygame
from character import Character
from ball import Ball
from random import randint


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    background = (0, 0, 200)
    pygame.display.set_caption("Blue Skies")
    character = Character(screen)
    ball = Ball(screen)
    lives = 3

    game_active = True
    moving_right = False
    moving_left = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_RIGHT:
                    moving_right = False

        if game_active:
            screen.fill(background)

            if moving_left and character.rect.left > 0:
                character.rect.x -= 2
            if moving_right and character.rect.right < 1200:
                character.rect.x += 2

            ball.fall()
            if ball.rect.top > 800:
                ball.rect.top = 0
                ball.rect.x = randint(50, 1100)
                lives -= 1
            elif ball.rect.colliderect(character.rect):
                ball.rect.top = 0
                ball.rect.x = randint(50, 1100)

            ball.blitme()
            character.blitme()
            pygame.display.flip()
            if lives == 0:
                game_active = False

        if game_active is False:
            sys.exit()


run_game()
