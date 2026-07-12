import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion  
class Ship:
    
    
    def __init__(self, game: 'AlienInvasion'):
        self.game = game  # Reference to the main game instance.
        self.settings = game.settings  # Access the shared settings.
        self.screen = game.screen  # Access the game screen.
        self.screen_rect = self.screen.get_rect()  # Get the rectangular area of the screen 

        # Load the ship image and scale 
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        # Get the rectangular area of the ship image 
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom  # Position the ship at the bottom center of the screen
        
    def draw(self):
             self.screen.blit(self.image, self.rect)  # determine where the  position is on the screen.