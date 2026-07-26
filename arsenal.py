"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Manage the player's bullet arsenal.
Date: 2026-07-26
"""

import pygame
from typing import TYPE_CHECKING

from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        # A sprite group makes it easy to update and manage all bullets together.
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_off_screen()

    def _remove_bullets_off_screen(self):
        # Use a copy because bullets can be removed during this loop.
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal.sprites():
            bullet.draw()

    def fire_bullet(self):
        # Do not let the player fill the whole screen with bullets.
        if len(self.arsenal) >= self.settings.bullets_amount:
            return False

        self.arsenal.add(Bullet(self.game))
        return True
