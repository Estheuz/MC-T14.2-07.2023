from dino_runner.utils.constants import SMALL_CACTUS


X_POS = 1250
Y_POS = 330
Y_POS_DUCK = 340
CACTUS_VEL = 4


class Cactus:
    def __init__(self):
        self.image_cactus =SMALL_CACTUS[0]

        self.cactus_rect = self.image_cactus.get_rect()
        self.cactus_rect.x = 850
        self.cactus_rect.y = Y_POS
        self.cactus_rect.x = X_POS

        self.step_count = 0
        
        self.cactus_run = True

        self.cactus_vel = CACTUS_VEL
    
    def update(self):
        
        if self.cactus_run:
            self.cactus()
        
        if self.step_count > 5:
            self.step_count = 0
    
    def cactus(self):
        self.image_cactus = SMALL_CACTUS[0]
        self.cactus_rect.y = Y_POS
        
        self.step_count+=1
    
    def draw(self, screen):
        self.cactus_rect.x -= CACTUS_VEL
        if self.cactus_rect.x < 5 :
            self.cactus_rect.x = 1200
        screen.blit(self.image_cactus,(self.cactus_rect.x, self.cactus_rect.y))