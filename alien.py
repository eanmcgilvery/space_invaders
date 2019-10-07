import pygame
from pygame.sprite import Sprite
from timer import *

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.my_timer = Timer(2)

        # Initalize an alien image
        self.image = pygame.image.load('images/alien_3-1.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

        if self.my_timer.frame_index():
            self.image = pygame.image.load('images/alien_3-1.png')
        else:
            self.image = pygame.image.load('images/alien_3-2.png')


    def blitme(self):
        """Draw the alien at its current location."""
        #for x in range(2):
        self.screen.blit(self.image, self.rect)



# class Alien1:
#     def __init__(self, point_value, image):
#         # Inheirit the Alien class
#
