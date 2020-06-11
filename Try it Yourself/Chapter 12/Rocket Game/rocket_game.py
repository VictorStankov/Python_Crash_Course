import pygame
import rocket
import game_functions as gf


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Rocket or idk")

    rocket_0 = rocket.Rocket(screen)

    while True:
        gf.check_events(rocket_0)
        rocket_0.update()
        gf.update_screen(screen, rocket_0)


run_game()
