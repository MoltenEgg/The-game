import pygame
import my_sprites

class Enemy:
    def __init__(self, type, alive_sprite, dead_sprite):
        self.type=type
        self.alive_sprite=alive_sprite
        self.dead_sprite=dead_sprite
    
    def draw_alive(self, surface, coor):
        x, y=coor
        surface.blit(self.alive_sprite, (x, y))
    
    def draw_dead(self, surface, coor):
        x, y=coor
        surface.blit(self.dead_sprite, (x, y))

goblin=Enemy('goblin', my_sprites.goblin, my_sprites.goblin_dead)
human=Enemy('human', my_sprites.human, my_sprites.human_dead)



