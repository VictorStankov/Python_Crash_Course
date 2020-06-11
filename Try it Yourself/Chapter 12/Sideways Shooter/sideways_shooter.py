import pygame
from pygame.sprite import Group
import sideways_ship
import s_settings as ss
import s_functions as fun


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sideways Shooter")
    settings = ss.Settings()

    ship = sideways_ship.Ship(settings, screen)
    bullets = Group()

    while True:
        fun.check_events(settings, screen, ship, bullets)
        ship.update()
        fun.update_bullets(bullets)
        fun.update_screen(settings, screen, ship, bullets)


run_game()
