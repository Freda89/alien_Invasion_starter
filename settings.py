from pathlib import Path

class Settings:
    # Store shared configuration values for the game.

    def __init__(self):
        self.name: str = "Alien Invasion"  # Game title shown in the window caption.
        self.screen_w: int = 1200  # Width of the game window in pixels.
        self.screen_h: int = 800  # Height of the game window in pixels.
        self.FPS: int = 60  # Target frames per second for the game loop.
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'  # Path to the background image file.

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'  # Path to the ship image file.
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5  # Speed at which the ship moves across the screen.
        

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'  # Path to the bullet image file.
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 5  # Speed at which bullets travel across the screen.
        self.bullet_w = 6
        self.bullet_h = 80
        self.bullets_amount = 3  # Maximum number of bullets allowed on screen at once.