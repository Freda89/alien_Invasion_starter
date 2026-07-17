import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game  # This is the main game object, like the controller for everything.
        self.settings = game.settings  # Settings are shared everywhere, so we just borrow them.
        self.screen = game.screen  # The screen where the aliens get drawn.
        self.fleet = pygame.sprite.Group()  # A squad of aliens all grouped together.
        self.fleet_direction = 1  # 1 means go right, -1 means go left. Easy.
        self.fleet_drop_speed = self.settings.fleet_drop_speed  # How fast the whole fleet drops when it hits an edge.

        self.create_fleet()  # Make the alien army show up at the start.

    def create_fleet(self):
        alien_w = self.settings.alien_w  # Width of one alien.
        alien_h = self.settings.alien_h  # Height of one alien.
        screen_w = self.settings.screen_w  # Screen width to see how much fits.
        screen_h = self.settings.screen_h  # Screen height so aliens don't go off-screen.

        fleet_w, fleet_h = self.calculate_fleet_size(
            alien_w, screen_w, alien_h, screen_h
        )  # Figure out rows and columns.

        x_offset, y_offset, vertical_spacing = self.calculate_offsets(
            alien_w, alien_h, screen_w, fleet_w
        )  # Center the fleet and space it out.

        
        self._create_rectangle_fleet(alien_w, alien_h,  fleet_w, fleet_h, x_offset, y_offset, )

    def _create_rectangle_fleet(
        self, alien_w, fleet_w, fleet_h, x_offset, y_offset, vertical_spacing
    ):
        for row in range(fleet_h):
            current_y = y_offset + row * vertical_spacing  # One row lower each time.
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset  # One column over each time.
                self._create_alien(current_x, current_y)  # Spawn an alien here.

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w):
        fleet_horizontal_space = fleet_w * alien_w  # Total space used by aliens.
        x_offset = int((screen_w - fleet_horizontal_space) / 2)  # Center it.
        y_offset = 10  # A little gap from the top.
        vertical_spacing = alien_h + 10  # Keep the rows from touching.
        return x_offset, y_offset, vertical_spacing

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = screen_w // alien_w  # How many aliens fit across.
        fleet_h = (screen_h // 2) // alien_h  # Use half the screen for aliens.

        if fleet_w % 2 == 0:
            fleet_w -= 1  # Make it odd so it doesn't look weird.
        else:
            fleet_w -= 2  # Leave some space on the sides.

        if fleet_h % 2 == 0:
            fleet_h -= 1  # Make the number of rows odd too.
        else:
            fleet_h -= 2  # Keep the aliens from being too jammed.

        return fleet_w, int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)  # Make a single alien.
        self.fleet.add(new_alien)  # Add it to the squad.

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()  # Draw every alien each frame.


