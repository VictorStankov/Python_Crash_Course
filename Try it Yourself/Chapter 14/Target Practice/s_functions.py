import sys
import pygame
from s_bullet import Bullet


def check_keydown_events(event, settings, screen, ship, bullets, play_button):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not settings.active:
            pygame.mouse.set_visible(False)
            settings.lives = 3
            settings.active = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(settings, screen, ship, bullets, play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets, play_button)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, bullets, target):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_colour)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    target.draw_target()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(bullets, settings):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.left >= 1200:
            bullets.remove(bullet)
            settings.lives -= 1
        if settings.lives == 0:
            settings.active = False


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)
