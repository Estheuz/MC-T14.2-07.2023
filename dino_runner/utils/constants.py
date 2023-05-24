import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

IMG_SCREEN_START = pygame.image.load(os.path.join(IMG_DIR, "Other/StartScreen.png"))

FONT_STYLE = "freesansbold.ttf"

#Constante obstaculos
OBSTACLE_Y_POS = 325

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanDash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanDash.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow1.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance2.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Arrow.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Arrow.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
