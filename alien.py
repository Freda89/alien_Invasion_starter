import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet  # Import the AlienFleet class for type checking.


class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()  # Initialize the Sprite superclass.

        self.screen = fleet.game.screen  # Reference to the game screen.
        self.boundaries = fleet.game.screen.get_rect()  # Get the rectangular area of the screen for boundary checks.
        self.settings = fleet.game.settings  # Access the shared settings.
        self.fleet = fleet  # Keep the fleet object so direction stays synced.

        self.image = pygame.image.load(self.settings.alien_file)  # Load the alien image.
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))  # Scale the alien image to the specified width and height.

        self.rect = self.image.get_rect()  # Get the rectangular area of the bullet image.
        self.rect.x = x  # Set the initial x-coordinate of the alien.
        self.rect.y = y  # Set the initial y-coordinate of the alien.

        self.y = float(self.rect.y)  # Store the alien's vertical position as a float for smooth movement.
        self.x = float(self.rect.x)  # Store the alien's horizontal position as a float for smooth movement.


        


    def update(self):
        temp_speed = self.settings.fleet_speed  # Get the ship's speed from settings.

        self.x += temp_speed * self.fleet.fleet_direction  # Move the alien horizontally based on the fleet direction.
        self.rect.x = self.x  # Update the alien's rect position based on the float value.
        self.rect.y = self.y  # Update the alien's rect position based on the float value.


    def check_edges(self):
        # Check if the alien has reached the edge of the screen.
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)  # Draw the bullet at its current position on the screen.