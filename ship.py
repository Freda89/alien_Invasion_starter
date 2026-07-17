import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.arsenal = arsenal

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom

        # These stay true while the player is holding an arrow key.
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        # Check the edges so the ship cannot leave the screen.
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def center_ship(self):
        # Use this when a new level starts.
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
