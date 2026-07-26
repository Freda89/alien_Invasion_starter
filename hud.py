"""Program: Alien Invasion
Author: Freda Acquah
Purpose: Render the heads-up display for scores, level, and ship lives.
Date: 2026-07-26
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:
    """Heads-up display: scores, level, and lives."""

    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20

        # Initialize images/rects
        self.update_scores()
        self.setup_life_image()
        self.update_level()

    def update_scores(self):
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self):
        score_str = f'Score: {self.game_stats.score:,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        max_score_str = f'Max score: {self.game_stats.max_score:,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.centerx = self.boundaries.centerx
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        hi_score_str = f'High score: {getattr(self.game_stats, "hi_score", 0):,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def setup_life_image(self):
        # Try to use the ship image for life icons, fallback to a solid square.
        try:
            img = pygame.image.load(self.settings.ship_file)
            img = pygame.transform.scale(img, (self.settings.ship_w // 2, self.settings.ship_h // 2))
            self.life_image = img.convert_alpha()
        except Exception:
            self.life_image = pygame.Surface((28, 28))
            self.life_image.fill(self.settings.text_color)

        self.update_lives()

    def update_lives(self):
        self.life_rects = []
        for i in range(self.game_stats.ship_left):
            life_rect = self.life_image.get_rect()
            life_rect.topleft = (
                self.padding + i * (life_rect.width + 10),
                self.boundaries.bottom - life_rect.height - self.padding,
            )
            self.life_rects.append(life_rect)

    def update_level(self):
        level_str = f'Level: {self.game_stats.level}'
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.topleft = (self.padding, self.padding + 40)

    def draw_lives(self):
        for life_rect in self.life_rects:
            self.screen.blit(self.life_image, life_rect)

    def draw(self):
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.draw_lives()
