import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion  
    from arsenal import Arsenal 



class Ship:
    
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal' = None):
        self.game = game  # Reference to the main game instance.
        self.settings = game.settings  # Access the shared settings.
        self.screen = game.screen  # Access the game screen.
        self.boudaries = self.screen.get_rect()  # Get the rectangular area of the screen for boundary checks.

        # Load the ship image and scale 
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        # Get the rectangular area of the ship image 
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom  # Position the ship at the bottom center of the screen
        self.moving_right = False  # Flag to keep track if the ship is moving right.
        self.moving_left = False  # Flag to keep track if the ship is moving left.
        self.x = float(self.rect.x)  # Store the ship's horizontal position as a float for smooth movement.
        self.arsenal = arsenal  # Reference to the Arsenal instance for managing bullets.

    def update(self):
        # Update the ship's position based on the current movement flags.
        self._update_ship_movement() 
        self.arsenal.update_arsenal()  # Update the position of bullets in the arsenal.

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed  # Get the ship's speed from settings.
        if self.moving_right and self.rect.right < self.boudaries.right:
            self.x += temp_speed  # Move the ship to the right.
        if self.moving_left and self.rect.left > 0:
            self.x -= temp_speed  # Move the ship to the left.

        self.rect.x = self.x # Update the ship's rect position based on the float value.

    def draw(self):
        self.arsenal.draw()  # Draw the bullets in the arsenal on the screen.
        self.screen.blit(self.image, self.rect)  # Draw the ship at its current position on the screen.

    def fire(self):
        return self.arsenal.fire_bullet()  # Attempt to fire a bullet from the ship's arsenal.
