import pygame
import os

# Global Constants
TITLE = "Maratona"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
pygame.mixer.init()

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
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-Shield1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-Shield2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-Hammer1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-Hammer2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-ShieldJump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-HammerJump.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanDash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanDash.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanShieldDash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/RomanShieldDash.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-HammerDash.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Roman-HammerDash.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zArrow1.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/zLance1.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Arrow.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Arrow.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/roman-shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/roman-sword.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

VICORY = pygame.image.load(os.path.join(IMG_DIR, 'Other/victory.png'))
START_SCREEN = pygame.image.load(os.path.join(IMG_DIR, 'Other/Start-Screen.png'))

LOSE_SCREEN = pygame.image.load(os.path.join(IMG_DIR, 'Other/lose.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"


SOUND_JUMP = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_jump.wav'))
SOUND_ATTACK = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_kick.wav'))
SOUND_UPGRADE = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_power-up.wav'))
SOUND_WIN = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_princess_help.wav'))
SOUND_LOSE = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_lost_a_life.wav'))
SOUND_DASH = pygame.mixer.Sound(os.path.join(IMG_DIR, 'Sounds/smw_yoshi_runs_away.wav'))