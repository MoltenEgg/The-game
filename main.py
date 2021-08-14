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

    screen.fill((56, 160, 153))

    #Шкала здоровья
    health_bar=pygame.Rect(ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y+66, health_bar_width_dinamic, 8)
    if health_bar_width_dinamic>=0.7*health_bar_width_stat:
        pygame.draw.rect(screen, (0, 255, 0), health_bar) #Рисуем шкалу здоровья
    elif health_bar_width_dinamic<0.7*health_bar_width_stat and health_bar_width_dinamic>=0.3*health_bar_width_stat:
        pygame.draw.rect(screen, (255, 255, 0), health_bar) #Рисуем шкалу здоровья
    else:
        pygame.draw.rect(screen, (255, 0, 0), health_bar)
    pygame.draw.rect(screen, (255, 255, 255), (health_bar.x, health_bar.y, health_bar_width_stat, 8), 2)

    #Рисую гоблина
    if Hp<=0:
        screen.blit(my_sprites.goblin_dead, (ENEMY_PLACEMENT))
    else:
        screen.blit(my_sprites.goblin, (ENEMY_PLACEMENT))
    pygame.display.update()

def main():
    Hp=50
    HpMAX=Hp
    RUN=True
    
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a and Hp>0:
                    Hp-=2
                if event.key == K_b and Hp<HpMAX:
                    Hp+=2


        drawing(Hp, HpMAX)        
        clock.tick(FPS)

if __name__ == '__main__':
    main()
