from pathlib import Path

class Settings:
    # Stuff that controls how the game looks and plays.

    def __init__(self):
        self.name: str = "Alien Invasion"  # The game title that shows up in the window.
        self.screen_w: int = 1200  # How wide the game window is.
        self.screen_h: int = 800  # How tall the game window is.
        self.FPS: int = 60  # Target frame rate so the game doesn’t go crazy fast.
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'  # Background image file.

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'  # Ship image file.
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5  # How fast the ship moves.
        

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'  # Bullet image file.
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'  # Sound to play when shooting.
        self.bullet_speed = 5  # Bullet speed so they fly up.
        self.bullet_w = 6
        self.bullet_h = 80
        self.bullets_amount = 3  # Max bullets on screen at once.

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'  # Alien image file.
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 2 # Speed at which the alien fleet moves.
