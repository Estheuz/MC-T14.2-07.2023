import random
from dino_runner.utils.constants import SCREEN_WIDTH

Y_POS = 380

class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(900, 1800)
        self.rect.y = 320
    
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.rect.x <-self.rect.width:
          self.rect.x = random.randint(900, 1800)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))