import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:

    def __init__(self): 
        pygame.init()  # Initialize Pygame 
        self.settings = Settings()  

        # game window with a fixed size.
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)  # the window title.
        

        self.bg = pygame.image.load(self.settings.bg_file)  # Load the background image.
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))  # Scale the background image to fit the screen.


        self.running = True  # Control whether the game loop continues.
        self.clock = pygame.time.Clock()  # Create a clock to manage the frame rate.

        self.ship = Ship(self)  # Create an instance of the Ship class for passing the game


    def run_game(self):
        # Start the main game loop.
        while self.running:
            # Process events requests.
            self._check_events()
            self.ship.update()  # Update the ship's position based on user input.         
            self._update_screen() 
            self.clock.tick(self.settings.FPS)  # Limit the frame rate to the target FPS.

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))  # Draw the background image onto the screen.
        self.ship.draw()  # Draw the ship on the screen.
        # Refresh the current frame on the display.
        pygame.display.flip()
        self.clock.tick(self.settings.FPS)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 




    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # Start moving the ship to the right.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  # Start moving the ship to the left.
        elif event.key == pygame.K_q:
            self.running = False  # Stop the game loop.
            pygame.quit()  # Quit Pygame.
            sys.exit()  # Exit the program.



if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()  # run the game.
