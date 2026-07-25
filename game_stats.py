from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Keep track of values that change while the game is running."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ship_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
        self.game_active = False

    def update(self, collisions):
        # update the player's score after aliens are hit
        self._update_score(collisions)
        self._update_max_score()

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
            print(f'Basic {self.socore}')

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            print(f'Max: {self.max_socore}')

    def update_level(self):
        self.level += 1
       # print(self.level)
    
      
