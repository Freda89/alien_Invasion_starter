import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game  # Reference to the main game instance.
        self.settings = game.settings  # Access the shared settings.
        self.fleet = pygame.sprite.Group()  # Create a group to hold all aliens in the fleet.
        self.fleet_direction = self.settings.fleet_direction  # Set the initial direction of the fleet 
        self.fleet_drop_speed = self.settings.fleet_drop_speed  # Set the speed at which the fleet drops down when it hits an edge.

        self._create_fleet()  # Create the initial fleet of aliens.

    def _create_fleet(self):
        alien_w = self.settings.alien_w  # Get the width of an alien from settings.
        screen_w = self.settings.screen_w  # Get the width of the screen from settings.

        fleet_w = self.calculate_fleet_size(alien_w, screen_w)  # Calculate how many aliens can fit in a row.

       
        fleet_horizontal_space = fleet_w * alien_w  # Calculate the total horizontal space occupied by the fleet.
        x_offset = int((screen_w - fleet_horizontal_space) / 2)  # Calculate the horizontal offset to center the fleet on the screen.

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset  # Calculate the x-coordinate for the current alien.
            self._create_alien(current_x, 10)  # Create an alien at the calculated position with a y-coordinate of 10.



    def calculate_fleet_size(self, alien_w, screen_w):
        fleet_w = screen_w//alien_w  # Calculate how many aliens can fit in a row based on the screen width and alien width.

        if fleet_w % 2 != 0:
            fleet_w -= 1  
        else:
            fleet_w -= 2 


        return fleet_w  # Return the calculated number of aliens that can fit in a row.



    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)  # Create a new alien instance at the specified position.

        self.fleet.add(new_alien)  # Add the new alien to the fleet group.

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()  # Draw each alien in the fleet on the screen.
