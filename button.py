"""Create the play button displayed before the game begins.
Autor: Fred Acquah
Link for button image: https://pngtree.com/free-png-vectors/play-button"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """Display an image-based button and detect clicks on it."""

    def __init__(self, game: 'AlienInvasion', msg):
        """Initialize the button image, rectangle, and position."""
        self.game = game
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings

        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._load_image()

    def _load_image(self):
        """Load and scale the play button image for the current screen."""
        image_path = self.settings.base_dir / 'Assets' / 'images' / 'Play button.png'
        self.image = pygame.image.load(str(image_path)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.image_rect = self.image.get_rect(center=self.rect.center)

    def draw(self):
        """Draw the play button image to the screen."""
        self.screen.blit(self.image, self.image_rect)

    def check_clicked(self, mouse_pos):
        """Return True when the mouse click is inside the button area."""
        return self.image_rect.collidepoint(mouse_pos)


    