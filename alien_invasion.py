import sys
import pygame
from pygame.mixer_music import play
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

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



        pygame.mixer.init()  # Initialize the mixer module for sound playback.
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))  # Load the laser sound effect.
        self.laser_sound.set_volume(0.5)  # Set the volume of the laser sound effect.

        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)  # Create an instance of the Ship class for passing the game and arsenal
        self.aliens = Alien(self, 10, 10)  # Create an instance of the Alien class for passing the game and initial position


    def run_game(self):
        # Start the main game loop.
        while self.running:
            # Process events requests.
            self._check_events()
            self.ship.update()  # Update the ship's position based on user input. 
            self.aliens.update()  # Update the alien's position based on game logic.        
            self._update_screen() 
            self.clock.tick(self.settings.FPS)  # Limit the frame rate to the target FPS.

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))  # Draw the background image onto the screen.
        self.aliens.draw_alien()  # Draw the alien on the screen.
        self.ship.draw()  # Draw the ship on the screen.
        self.aliens.draw_alien()  # Draw the alien on the screen.
        # Refresh the current frame on the display.
        pygame.display.flip()

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
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():  # Attempt to fire a bullet from the ship's arsenal.
                self.laser_sound.play()  # Play the laser sound effect if a bullet was successfully fired.
                self.laser_sound.fadeout(250)  # Fade out the laser sound effect after 100 milliseconds.
        elif event.key == pygame.K_q:
            self.running = False  # Stop the game loop.
            pygame.quit()  # Quit Pygame.
            sys.exit()  # Exit the program.



if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()  # run the game.
