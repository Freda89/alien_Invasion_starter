import sys
import pygame

class AlienInvasion:

    def __init__(self): 
        pygame.init()  # Initialize Pygame 
        # game window with a fixed size.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")  # the window title.

        self.running = True  # Control whether the game loop continues.

    def run_game(self):
        # Start the main game loop.
        while self.running:
            # Process events requests.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            # Refresh the current frame on the display.
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion() 
    ai.run_game()  # run the game.
