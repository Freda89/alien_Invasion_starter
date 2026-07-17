import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion  # Import the AlienInvasion class for type checking.


class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        super().__init__()  # Initialize the Sprite superclass.

        self.screen = game.screen  # Reference to the game screen.
        self.boundaries = game.screen.get_rect()  # Get the rectangular area of the screen for boundary checks.
        self.settings = game.settings  # Access the shared settings.

        self.image = pygame.image.load(self.settings.alien_file)  # Load the alien image.
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))  # Scale the alien image to the specified width and height.

        self.rect = self.image.get_rect()  # Get the rectangular area of the bullet image.
        self.rect.x = x  # Set the initial x-coordinate of the alien.
        self.rect.y = y  # Set the initial y-coordinate of the alien.


        


    def update(self):
       pass

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)  # Draw the bullet at its current position on the screen.