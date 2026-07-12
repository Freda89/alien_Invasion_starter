from pathlib import Path

class Settings:
    # Store shared configuration values for the game.

    def __init__(self):
        self.name: str = "Alien Invasion"  # Game title shown in the window caption.
        self.screen_w: int = 1200  # Width of the game window in pixels.
        self.screen_h: int = 800  # Height of the game window in pixels.
        self.FPS: int = 60  # Target frames per second for the game loop.
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'  # Path to the background image file.