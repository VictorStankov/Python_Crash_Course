import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class Raindrop(Sprite):
    def __init__(self, screen):
        super(Raindrop, self).__init__()
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width
        self.screen = screen


def fill_with_stars(screen, raindrops):
    raindrop = Raindrop(screen)
    raindrop_width = raindrop.rect.width
    raindrop_height = raindrop.rect.height
    available_space_y = 800
    number_rows = int(available_space_y / (2 * raindrop_height))
    available_space_x = 1200 - 2 * raindrop_width
    number_stars_x = int(available_space_x / (2 * raindrop.width))

    for row in range(number_rows):
        for number in range(number_stars_x):
            raindrop = Raindrop(screen)
            raindrop.x = raindrop_width + 2 * raindrop_width * number + randint(-10, 10)
            raindrop.rect.x = raindrop.x
            raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row + randint(-10, 10)
            raindrops.add(raindrop)

    raindrops.draw(screen)
    pygame.display.flip()


def move_raindrops(raindrops, screen_rect, screen):
    for raindrop in raindrops.sprites():
        raindrop.rect.y += 1
        raindrop.y = raindrop.rect.y
        if raindrop.rect.top >= screen_rect.bottom:
            raindrop.remove()
            fill_with_stars(screen, raindrops)

    pygame.display.flip()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Stars")
    screen.fill((255, 255, 255))
    screen_rect = screen.get_rect()
    raindrops = Group()
    fill_with_stars(screen, raindrops)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        move_raindrops(raindrops, screen_rect, screen)


run_game()
