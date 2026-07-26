"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Track score, level, lives, high-score data for the game.
Date: 2026-07-26
"""

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Keep track of values that change while the game is running."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()


    def init_saved_scores(self):
        self.path = self.settings.scores_file
        self.path.parent.mkdir(parents=True, exist_ok=True)

        if self.path.exists():
            contents = self.path.read_text()
            if contents:
                try:
                    scores = json.loads(contents)
                except json.JSONDecodeError:
                    scores = {}
                self.hi_score = scores.get('hi_score', 0)
            else:
                self.hi_score = 0
                self.save_score()
        else:
            self.hi_score = 0
            self.save_score()

    def save_score(self):
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(contents)

    def save_scores(self):
        self.save_score()

    def reset_stats(self):
        self.ship_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
        self.game_active = False

    def update(self, collisions):
        # update the player's score after aliens are hit
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions):
        for collided_aliens in collisions.values():
            self.score += self.settings.alien_points * len(collided_aliens)
            print(f'Basic {self.score}')

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
            # print(f'Max: {self.max_score}')

    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
            # print(f'Max: {self.max_score}')

    def update_level(self):     
        self.level += 1
        # print(self.level)
    
      
