import pygame


class Target:
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen):
        """Create a bullet object at the ship's current position."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.colour = (0, 255, 0)

    def update(self, settings):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        if self.rect.top <= 0 or self.rect.bottom >= 800:
            settings.direction *= -1
        self.y += 0.5 * settings.direction
        # Update the rect position.
        self.rect.y = self.y

    def draw_target(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
