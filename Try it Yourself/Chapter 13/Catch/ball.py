import pygame
from random import randint


class Ball:
    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = randint(50, 1150)
        self.rect.top = self.screen_rect.top
        self.rect.y = 0
        self.y = self.rect.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def fall(self):
        self.y += 1
        self.rect.y += 1
