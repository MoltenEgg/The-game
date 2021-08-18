import pygame
pygame.init()

goblin=pygame.image.load('assets/goblin.png')
goblin_dead=pygame.image.load('assets/goblin_dead.png')
under_enemy=pygame.image.load('assets/under_enemy.png')
human=pygame.image.load('assets/human.png')
human_dead=pygame.image.load('assets/human_dead.png')

HIT_SOUND=pygame.mixer.Sound('assets/hit_sound.wav')
DYING_SOUND=pygame.mixer.Sound('assets/dying_sound.wav')