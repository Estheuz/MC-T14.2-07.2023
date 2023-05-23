import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles1 = []
        self.obstacles2 = []
    
    def update(self, game):
        if len(self.obstacles1) == 0:
            self.obstacles1.append(Cactus(SMALL_CACTUS[random.randint(0, 2)]))
            self.obstacles2.append(Cactus(LARGE_CACTUS[random.randint(0, 2)]))
        
        for obstacle in self.obstacles1:
            obstacle.update(game.game_speed, self.obstacles1)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(200)
               # game.playing = False

        for obstacle in self.obstacles2:
            obstacle.update(game.game_speed, self.obstacles2)
            
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(200)
              #  game.playing = False
            
        
    def draw(self,screen):
        for obstacle in self.obstacles1:
            obstacle.draw(screen)

        for obstacle in self.obstacles2:
            obstacle.draw(screen)