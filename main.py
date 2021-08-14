import pygame
import sys

from pygame.locals import *
import my_sprites



pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption("The best game")
SIZE=WIDTH, HEIGHT=640, 480
screen=pygame.display.set_mode(SIZE)


FPS=60
ENEMY_PLACEMENT=ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y=(40, 40)
 #тестовое значение здоровья



def drawing(Hp, HpMAX):
    health_bar_width_stat=64
    health_bar_width_dinamic=health_bar_width_stat*Hp//HpMAX

    screen.fill((0, 0, 0))
    health_bar=pygame.Rect(ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y+66, health_bar_width_dinamic, 8)
    pygame.draw.rect(screen, (0, 255, 0), health_bar)
    pygame.draw.rect(screen, (255, 255, 255), (health_bar.x, health_bar.y, health_bar_width_stat, 8), 2)
    screen.blit(my_sprites.goblin, (ENEMY_PLACEMENT))
    pygame.display.update()

def main():
    Hp=37
    HpMAX=Hp
    RUN=True
    
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    Hp-=5
                if event.key == K_b:
                    Hp+=5


        drawing(Hp, HpMAX)        
        clock.tick(FPS)

if __name__ == '__main__':
    main()
