import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """A simple button for the game screen with text and click detection."""

    def __init__(self, game: 'AlienInvasion', msg):
        # save the main game object so we can access the screen and settings
        self.game = game
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings

        # set up the font and button size from settings
        self.font = pygame.font.Font(self.settings.font_file, self.settings.buttons_font_size)
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center

        # make the text image for the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # render the text into an image so pygame can draw it
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        # fill the button rectangle and then draw the text on top
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        # check if the mouse click is inside the button area
        return self.rect.collidepoint(mouse_pos)


    