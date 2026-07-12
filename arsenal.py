import pygame
from typing import TYPE_CHECKING

from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion  # Import the AlienInvasion class for type checking.
    from bullet import Bullet  # Import the Bullet class for type checking.
    

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game  # Reference to the main game instance.
        self.settings = game.settings  # Access the shared settings.
        self.arsenal = pygame.sprite.Group()  # Create a group to hold all bullets fired by the ship.


    def update_arsenal(self):
        self.arsenal.update()  # Update the position of all bullets in the arsenal.
        self._remove_bullets_off_screen()

    def _remove_bullets_off_screen(self):
        for bullet in self.arsenal.copy():  # Iterate over a copy of the arsenal to avoid modifying it while iterating.
            if bullet.rect.bottom <= 0:  # Check if the bullet has moved off the top of the screen.
                self.arsenal.remove(bullet)  # Remove the bullet from the arsenal group.

    def draw(self):
        for bullet in self.arsenal.sprites():
            bullet.draw()  # Draw each bullet in the arsenal on the screen.

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_amount:  # Check if the number of bullets on screen is less than the allowed amount.
            new_bullet = Bullet(self.game)  # Create a new bullet instance.
            self.arsenal.add(new_bullet)  # Add the new bullet to the arsenal group.
            return True
        return False
        
       