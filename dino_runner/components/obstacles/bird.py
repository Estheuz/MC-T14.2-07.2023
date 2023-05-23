
from dino_runner.utils.constants import BIRD

X_POS = 1200
Y_POS = 600
BIRD_VEL = 7


class Bird:
    def __init__(self):
        self.image_bird = BIRD[0]
        self.bird_rect = self.image_bird.get_rect()

        self.bird_rect.y = Y_POS
        self.bird_rect.x = X_POS

        self.step_count = 0
        self.bird_run = True
        self.bird_vel = BIRD_VEL


    def update(self):
        
        if self.bird_run:
            self.bird()
        
        if self.step_count > 5:
            self.step_count = 0

        
        if self.bird_rect.y <= 100:
            self.bird_down = True
            self.bird_up = False
            self.move()

        elif self.bird_rect.y >= 300:
            self.bird_down = False
            self.bird_up = True
            self.move()
        
    
    def bird(self):
        self.image_bird = BIRD[self.step_count//3]
        self.step_count+=1
    
    def draw(self, screen):
        self.bird_rect.x -= BIRD_VEL 
        self.bird_rect.y -= BIRD_VEL
        if self.bird_rect.x < 6:
          self.bird_rect.x = 1200

        
        screen.blit(self.image_bird,(self.bird_rect.x, self.bird_rect.y))

    def move(self):
        if self.bird_up == True and self.bird_down == False:
            self.bird_rect.y -= BIRD_VEL

        elif self.bird_down == True and self.bird_up == False:
            self.bird_rect.y += BIRD_VEL



