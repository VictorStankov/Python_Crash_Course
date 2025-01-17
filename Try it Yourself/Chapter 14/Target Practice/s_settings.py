class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
        self.direction = 1
        self.lives = 3
        self.active = False
