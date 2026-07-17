import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        # Keeping aliens in one group lets us move them as a team.
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = 1  # 1 is right and -1 is left.
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(
            alien_w, screen_w, alien_h, screen_h
        )

        x_offset, y_offset, vertical_spacing = self.calculate_offsets(
            alien_w, alien_h, screen_w, fleet_w
        )

        self._create_rectangle_fleet(
            alien_w, fleet_w, fleet_h, x_offset, y_offset, vertical_spacing
        )

    def _create_rectangle_fleet(
        self, alien_w, fleet_w, fleet_h, x_offset, y_offset, vertical_spacing
    ):
        for row in range(fleet_h):
            current_y = y_offset + row * vertical_spacing
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w):
        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((screen_w - fleet_horizontal_space) / 2)
        y_offset = 10
        vertical_spacing = alien_h + 10  # Give each row a small gap.
        return x_offset, y_offset, vertical_spacing

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

    def _check_fleet_edges(self):
        # If one alien hits an edge, the whole group goes down and turns around.
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        # Move every alien down together to make the group look like one fleet.
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y


    def update_fleet(self):
        # Check the edge first, then move the aliens for this frame.
        self._check_fleet_edges()
        self.fleet.update()


    def draw(self):
        alien: Alien
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """Remove aliens and sprites from another group when they overlap."""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        """Return True if any alien has reached the bottom of the screen."""
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
