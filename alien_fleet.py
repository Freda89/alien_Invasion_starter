import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game  # Reference to the main game instance.
        self.settings = game.settings  # Access the shared settings.
        self.screen = game.screen  # Game screen where aliens are drawn.
        self.fleet = pygame.sprite.Group()  # Group that holds all aliens in the fleet.
        self.fleet_direction = 1  # Initialize the fleet direction (1 for right, -1 for left).
        self.fleet_drop_speed = self.settings.fleet_drop_speed  # Set the speed at which the fleet drops down when it reaches an edge.

        self.create_fleet()  # Create the initial alien fleet on the screen.

    def create_fleet(self):
        alien_w = self.settings.alien_w  # Get the width of an alien from settings.
        alien_h = self.settings.alien_h  # Get the height of an alien from settings.
        screen_w = self.settings.screen_w  # Get the width of the screen from settings.
        screen_h = self.settings.screen_h  # Get the height of the screen from settings.

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)  # Calculate the number of aliens that can fit in a row and a column.

        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((screen_w - fleet_horizontal_space) / 2)

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            if col % 2 == 0:
                continue
            self._create_alien(current_x, 10)

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h // 2) // alien_h

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        
        return fleet_w, int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()


