from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, IMG_SCREEN_START

import pygame
class Text:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.playing = False
        self.executing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.score = 0
        self.high_score = 0
        self.death_count = 0
