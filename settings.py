"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Define game settings, screen dimensions, and asset paths for the Alien Invasion project.
Date: 2026-07-26
"""

from pathlib import Path


class Settings:
    # This is the one place to change the game's sizes and speeds.

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60  
        self.bg_file = self.base_dir / 'Assets' / 'images' / 'Background.png'
        self.difficulty_scale = 1.1
        self.scores_file = self.base_dir / 'Assets' / 'files' / 'scores.json'

        self.ship_file = self.base_dir / 'Assets' / 'images' / 'Ship.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_file = self.base_dir / 'Assets' / 'images' / 'LaserBlast.png'
        self.laser_sound = self.base_dir / 'Assets' / 'sound' / 'laser.mp3'
        self.background_music = self.base_dir / 'Assets' / 'sound' / 'backgroundmusic.mp3'
        self.bullet_speed = 5
        
        self.bullets_amount = 3  # This stops the player from shooting unlimited lasers.

        self.alien_file = self.base_dir / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 1
        self.fleet_drop_speed = 20  # Bigger number means the aliens get closer faster.


        self.button_w = 200
        self.button_h = 50 
        self.button_color = (44,32,158)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = self.base_dir / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Expanded.ttf'


    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3
        self.bullet_w = 6
        self.bullet_h = 80
        self.bullet_speed = 5
        self.bullets_amount = 3

        self.fleet_speed = 1
        self.fleet_drop_speed = 20
        self.alien_points = 50 

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
