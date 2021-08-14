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
    #Переменные
    health_bar_width_stat=64
    health_bar_width_dinamic=health_bar_width_stat*Hp//HpMAX
    health_font=pygame.font.SysFont('Engravers MT', 10)
    health_bar_text=health_font.render((str(Hp)+'/'+str(HpMAX)), True, (0, 0, 0))

    #Само рисование
    screen.fill((56, 160, 153))

    #Шкала здоровья
    health_bar=pygame.Rect(ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y+70, health_bar_width_dinamic, 8)
    if health_bar_width_dinamic>=0.7*health_bar_width_stat:
        pygame.draw.rect(screen, (0, 255, 0), health_bar) #Рисуем шкалу здоровья
    elif health_bar_width_dinamic<0.7*health_bar_width_stat and health_bar_width_dinamic>=0.3*health_bar_width_stat:
        pygame.draw.rect(screen, (255, 255, 0), health_bar) #Рисуем шкалу здоровья
    else:
        pygame.draw.rect(screen, (255, 0, 0), health_bar)
    pygame.draw.rect(screen, (255, 255, 255), (health_bar.x, health_bar.y, health_bar_width_stat, 8), 2)
    screen.blit(health_bar_text, (health_bar.x+health_bar_width_stat+10, health_bar.y))

    #Под врагом
    screen.blit(my_sprites.under_enemy, (ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y+10)) 
    #Рисую гоблина
    
    if Hp<=0:
        screen.blit(my_sprites.goblin_dead, (ENEMY_PLACEMENT))
    else:
        screen.blit(my_sprites.goblin, (ENEMY_PLACEMENT))

    pygame.display.update()

def main():
    Hp=37
    HpMAX=Hp
    RUN=True
    HIT_SOUND=pygame.mixer.Sound('assets/hit_sound.wav')
    DYING_SOUND=pygame.mixer.Sound('assets/dying_sound.wav')
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a and Hp>0:                
                    if Hp-5>0:
                        HIT_SOUND.play()
                        Hp-=5
                    else:
                        DYING_SOUND.play()
                        Hp-=5
                if event.key == K_b and Hp<HpMAX:
                    Hp+=5


        drawing(Hp, HpMAX)        
        clock.tick(FPS)

if __name__ == '__main__':
    main()
