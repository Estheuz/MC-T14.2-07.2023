import pygame, random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, BIRD
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bird import Bird
from dino_runner.components.cactus import Cactus

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.contador = 0
        self.player = Dinosaur()
        self.enemy_bird = Bird()
        self.enemy_cactus = Cactus()

        self.fonte= pygame.font.SysFont('arial', 30, True, True)
 
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.coor_clouds = []

        for cl in range(6):
         self.x_pos_cloud = random.randint(0, 1000)
         self.y_pos_cloud = random.randint(0, 200)
         self.coor_clouds.append([self.x_pos_cloud, self.y_pos_cloud])


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.contador = self.contador + 1
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_bird.update()
        self.enemy_cactus.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.crono()
        self.player.draw(self.screen)
        self.enemy_bird.draw(self.screen)
        self.enemy_cactus.draw(self.screen)
        
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        for position_cloud in self.coor_clouds:
       
            self.screen.blit(CLOUD, position_cloud)
            position_cloud[0] -= 0.8
            if position_cloud[0] < -55:
                position_cloud[0] = 1150
    def crono(self):
         self.mensagem = f'{self.contador}m'
         self.texto_formatado = self.fonte.render(self.mensagem, False, (0,0,0))
         self.screen.blit(self.texto_formatado, (800,32))