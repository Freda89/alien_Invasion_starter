import sys

import pygame

from alien_fleet import AlienFleet
from arsenal import Arsenal
from settings import Settings
from game_stats import GameStats
from ship import Ship
from time import sleep
from button import Button
from hud import HUD


class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()
        self.settings.initialize_dynamic_settings()
        self.game_stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)
        self.clock = pygame.time.Clock()
        self.running = True
        self.HUD = HUD(self)

        # Load the background once so the game does not have to reload it every frame.
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.5)

        # These objects hold the player, bullets, and aliens for the whole game.
        self.arsenal = Arsenal(self)
        self.ship = Ship(self, self.arsenal)

        self.play_button = Button(self, 'Play')
        self.alien_fleet = AlienFleet(self)

    def run_game(self):
        # Keep repeating these steps until the player closes the game.
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien_fleet.update_fleet()
            self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        # A bullet and alien disappear when their rectangles touch.
        collisions = pygame.sprite.groupcollide(
            self.arsenal.arsenal, self.alien_fleet.fleet, True, True
        )
        if collisions:
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        # Start a fresh wave after the player clears every alien.
        if not self.alien_fleet.fleet:
            # advance difficulty and level when the wave is cleared
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_scores()
            self.HUD.update_level()
            self._reset_level()
            return

        # The level also restarts if an alien hits the ship or reaches the bottom.
        ship_hit = pygame.sprite.spritecollideany(self.ship, self.alien_fleet.fleet)
        alien_reached_bottom = any(
            alien.rect.bottom >= self.screen.get_rect().bottom
            for alien in self.alien_fleet.fleet
        )
        if ship_hit or alien_reached_bottom:
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            self.HUD.update_scores()
            self.HUD.update_level()
            # update HUD view

    def _reset_level(self):
        # Clear old sprites, put the ship back in the middle, and make a new fleet.
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.ship.center_ship()
        self.alien_fleet.create_fleet()


    def restart_game(self):
        # reset the game state and start fresh
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self.HUD.update_level()
        self._reset_level()
        self.ship.center_ship()
        self.game_stats.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        # Draw the background first, then the sprites on top of it.
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()


        if not self.game_stats.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        # Turn keyboard events into movement or shooting actions.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_stats.save_scores()
                self._quit_game()
            elif event.type == pygame.KEYDOWN and self.game_stats.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE and self.ship.fire():
            # Only play the sound when a bullet was actually created.
            self.laser_sound.play()
        elif event.key == pygame.K_q:
                self.game_stats.save_scores()

    def _quit_game(self):
        # Stop Pygame cleanly before ending the program.
        self.running = False
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    AlienInvasion().run_game()
