"""Manage the alien fleet's custom pattern and movement.
Author: Freda Acquah
"""

import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Coordinate the alien fleet and its movement across the screen."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the fleet and create its initial formation."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = 1
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create a custom wedge formation of aliens for the current level."""
        row_widths = self._build_wedge_rows()
        self._create_patterned_fleet(row_widths)

    def _build_wedge_rows(self) :
        """Return the row sizes that define the wedge-shaped fleet pattern."""
        return [3, 4, 5, 6, 5, 4, 3]

    def _create_patterned_fleet(self, row_widths: list[int]):
        """Create every alien in the fleet using the supplied row widths."""
        self.fleet_direction = 1
        vertical_spacing = self.settings.alien_h + 18
        starting_y = 70

        for row_index, row_width in enumerate(row_widths):
            row_pixels = row_width * self.settings.alien_w + (row_width - 1) * 10
            starting_x = (self.settings.screen_w - row_pixels) // 2
            current_y = starting_y + row_index * vertical_spacing

            for column_index in range(row_width):
                current_x = starting_x + column_index * (self.settings.alien_w + 10)
                self._create_alien(current_x, current_y)

    def _create_alien(self, current_x: float, current_y: float):
        """Create and add one alien sprite to the fleet."""
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Reverse the fleet direction and drop it when one alien reaches an edge."""
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Move every alien down together to preserve the fleet movement effect."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y

    def update_fleet(self):
        """Check the fleet edges and move the fleet for the current frame."""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw every alien in the fleet to the screen."""
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Remove aliens and sprites from another group when their masks overlap."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        """Return True when any alien reaches the bottom edge of the screen."""
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
