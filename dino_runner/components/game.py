import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, FONT_STYLE, IMG_SCREEN_START
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.text import Text
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.the_text = Text()
        
        self.playing = False
        self.executing = False
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        
        self.cloud_y_pos = random.randint(100, 250)
        self.cloud_x_pos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100)
        
    def execute(self):
        self.executing = True
        #condicional por contador de morte
        #se o contador for igual a zero 'primeira tela'
        #Se for maior, aí vem os bagulho
        while self.executing:
            
            if not self.playing:
                self.display_menu()
        
        pygame.quit()    
    
    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.update_score()
        self.update_speed()
        self.obstacle_manager.update(self)
        
    def update_score(self):
        self.score+=1

        if self.score > self.high_score:
            self.high_score = self.score

    def update_speed(self):
        if self.score % 300 == 0:
            self.game_speed += 5
        
    def draw_speed(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"speed: {self.game_speed}", True, (0,0,0))
        self.screen.blit(text, (100, 39))

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_simple_cloud()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_speed()
        self.obstacle_manager.draw(self.screen)
        
        pygame.display.flip()

    def display_menu(self):
        self.screen.fill((255, 255, 255))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        
        
        font = pygame.font.Font(FONT_STYLE, 22)


        if self.death_count > 0 :
            text_death_count  = font.render(f'(death count :  {self.death_count})', True, (0,0,0))
            self.screen.blit(text_death_count, (460, 300))
            
            text_death_count  = font.render(f'(High Score :  {self.high_score})', True, (0,0,0))
            self.screen.blit(text_death_count, (460, 200))

            text_death_count  = font.render(f'Space- to continue', True, (0,0,0))
            self.screen.blit(text_death_count, (300, 450))

            text_death_count  = font.render(f'X- to reset', True, (0,0,0))
            self.screen.blit(text_death_count, (700, 450))

        else:
         text = font.render("Press space to start", True, (0,0,0))
         text_rect = text.get_rect()
         text_rect.center = (x_text_pos, y_text_pos)
         self.screen.blit(text, text_rect)

        self.menu_events_handler()
        pygame.display.flip()
    
    def menu_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
                self.playing = False
                
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE] :
                self.run()

        if keys_pressed[pygame.K_x] :
                self.score = 0
                self.high_score = 0
                self.death_count = 0
                self.run()
                 
    
    def draw_score(self):
        
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000,50)

        text2 = font.render(f"HighScore: {self.high_score}", True, (0,0,0))
        
        self.screen.blit(text, text_rect)
        self.screen.blit(text2, (500, 40))
        
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_simple_cloud(self):
        cloud_image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        if self.cloud_x_pos <= -cloud_image_width:
            self.cloud_x_pos = SCREEN_WIDTH + random.randint(0,50)
            self.cloud_y_pos = random.randint(100, 250)
            self.screen.blit(CLOUD, (self.cloud_x_pos, self.cloud_y_pos))
        
        self.cloud_x_pos -=self.game_speed
    
    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 20
            
            
        
        