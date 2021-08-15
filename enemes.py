import pygame
import my_sprites

class Enemy:
    def __init__(self, type, alive_sprite, dead_sprite):
        self.type=type
        self.alive_sprite=alive_sprite
        self.dead_sprite=dead_sprite
    
    def draw_alive(self, surface, x, y):
        surface.blit(self.alive_sprite, (x, y))


goblin=Enemy('goblin', my_sprites.goblin, my_sprites.goblin_dead)




