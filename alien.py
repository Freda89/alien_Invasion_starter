"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Define the alien movement behavior for the game fleet.
Date: 2026-07-26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()

        self.screen = fleet.game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = fleet.game.settings
        # The alien checks the fleet for the direction it should move.
        self.fleet = fleet

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Floats help movement stay smooth instead of jumping between pixels.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)


        


    def update(self):
        self.x += self.settings.fleet_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y


    def check_edges(self):
        return self.rect.right >= self.boundaries.right or self.rect.left <= 0

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
