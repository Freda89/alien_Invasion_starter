"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Define the bullet sprite used by the player's ship.
Date: 2026-07-26
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        # A float keeps bullet movement smooth even with smaller speeds later.
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
