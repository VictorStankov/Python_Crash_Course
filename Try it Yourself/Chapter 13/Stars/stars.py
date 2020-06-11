import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from random import randint


class Stars(Sprite):
    def __init__(self):
        super(Stars, self).__init__()
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width


def fill_with_stars(screen, stars):
    star = Stars()
    star_width = star.rect.width
    star_height = star.rect.height
    available_space_y = 800
    number_rows = int(available_space_y / (2 * star_height))
    available_space_x = 1200 - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star.width))

    for row in range(number_rows):
        for number in range(number_stars_x):
            star = Stars()
            star.x = star_width + 2 * star_width * number + randint(-10, 10)
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * row + randint(-10, 10)
            stars.add(star)

    stars.draw(screen)
    pygame.display.flip()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Stars")
    screen.fill((182, 185, 183))
    stars = Group()
    fill_with_stars(screen, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


run_game()
