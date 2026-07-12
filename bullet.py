import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion  # Import the AlienInvasion class for type checking.


class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()  # Initialize the Sprite superclass.

        self.screen = game.screen  # Reference to the game screen.
        self.settings = game.settings  # Access the shared settings.

        self.image = pygame.image.load(self.settings.bullet_file)  # Load the bullet image.
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))  # Scale the bullet image to the specified width and height.

        self.rect = self.image.get_rect()  # Get the rectangular area of the bullet image.
        self.rect.midtop = game.ship.rect.midtop  # Position the bullet at the top center of the ship's rectangle.
        self.y = float(self.rect.y)  # Store the bullet's vertical position.

    def update(self):
        self.y -= self.settings.bullet_speed  # Move the bullet upward by decreasing its y-coordinate.
        self.rect.y = self.y  # Update the bullet's rect position based on the float value.

    def draw(self):
        self.screen.blit(self.image, self.rect)  # Draw the bullet at its current position on the screen.