import pygame
import sys

from pygame.locals import *
import my_sprites, menu
import enemes



pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()
pygame.display.set_caption("The best game")
SIZE=WIDTH, HEIGHT=640, 480
screen=pygame.display.set_mode(SIZE)



FPS=60
ENEMY_PLACEMENT=ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y=(400, 80)
 #тестовое значение здоровья



def drawing(Hp, HpMAX, m1_down):
    #Переменные
    health_bar_width_stat=64
    health_bar_width_dinamic=health_bar_width_stat*Hp//HpMAX
    health_font=pygame.font.SysFont('Engravers MT', 10)
    menu_font=pygame.font.SysFont('Engravers MT', 14)
    health_bar_text=health_font.render((str(Hp)+'/'+str(HpMAX)), True, (0, 0, 0))
    attack_button_text=menu_font.render(('attack'), True, (255, 255, 255))
    heal_button_text=menu_font.render(('heal'), True, (255, 255, 255))
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
        enemes.goblin.draw_dead(screen, ENEMY_PLACEMENT)
    else:
        enemes.goblin.draw_alive(screen, ENEMY_PLACEMENT)

    
    #Меню
    
       

def main():
    Hp=37
    HpMAX=Hp
    RUN=True
    HIT_SOUND=pygame.mixer.Sound('assets/hit_sound.wav')
    DYING_SOUND=pygame.mixer.Sound('assets/dying_sound.wav')
    HEAL_SOUND=pygame.mixer.Sound('assets/healing_sound.wav')
    global m1_down
    m1_down=False
    button=[]
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_a and Hp>0:                
                    if Hp-5>0:
                        HIT_SOUND.play()
                    else:
                        DYING_SOUND.play()
                    Hp-=5                    
                if event.key == K_b and Hp<HpMAX:
                    Hp+=5
            if event.type ==pygame.MOUSEBUTTONDOWN:
               m1_down=True
               
            if event.type ==pygame.MOUSEBUTTONUP:
               m1_down=False
               #m1_down=False
            
            drawing(Hp, HpMAX, m1_down)
            button=menu.menu(m1_down)
            if button[0]==True:
                if Hp-5>0:
                    HIT_SOUND.play()
                else:
                     DYING_SOUND.play()
                Hp-=5
            if button[1]==True:
                Hp+=5
                HEAL_SOUND.play()
            
            pygame.display.update()
            clock.tick(FPS)
    
def hit(Hp):
    Hp-=5
    my_sprites.HIT_SOUND.play()
    return Hp

if __name__ == '__main__':
    main()
