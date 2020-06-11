import pygame
from pygame.sprite import Group
import sideways_ship
from s_settings import Settings
import s_functions as fun
from target import Target
from button import Button


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sideways Shooter")
    settings = Settings()
    target = Target(screen)
    play_button = Button(settings, screen, "Play")

    ship = sideways_ship.Ship(settings, screen)
    bullets = Group()
    target.draw_target()
    fun.update_screen(settings, screen, ship, bullets, target)

    while True:
        fun.check_events(settings, screen, ship, bullets, play_button)

        if settings.active:
            ship.update()
            fun.update_bullets(bullets, settings)
            fun.update_screen(settings, screen, ship, bullets, target)
            target.update(settings)
        else:
            pygame.mouse.set_visible(True)
            play_button.draw_button()

            pygame.display.flip()


run_game()
