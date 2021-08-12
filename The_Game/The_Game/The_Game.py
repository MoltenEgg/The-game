import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()

HP_FONT=pygame.font.SysFont('Britannic Bold', 30)
MENU_FONT=pygame.font.SysFont('Arial', 15)
attack_button_text=pygame.font.Font.render(MENU_FONT,'attack', True, (255, 255, 255))


clock=pygame.time.Clock()

WINDOW_SIZE = (400, 400)

pygame.display.set_caption("THE Game")
screen=pygame.display.set_mode(WINDOW_SIZE, 0, 32)
goblo_image=pygame.image.load('Goblo2.png') #160x240
goblo_dead_image=pygame.image.load('Goblo2dead.png') #240x160
Goblo_state=((goblo_image, (90, 170)), (goblo_dead_image, (90, 170)))

HP=37
HPmax=37
health_color = (0, 0, 0)

while True: #Game Loop
    screen.fill((0, 0, 0)) #заполнил экран

    health=HP/HPmax*100 #отслеживаю HP
    HP_counter_text=pygame.font.Font.render(HP_FONT, (str(HP)+"/"+str(HPmax)+'HP'), True, (255, 255, 255))

    if health >0:
        screen.blit(goblo_image, (170, 100)) #рисую гобла
    else:
        screen.blit(goblo_dead_image, (170, 180))

    #Шкала здоровья
    Health_Bar_Border=pygame.draw.rect(screen, (255, 255, 255), (200, 250, 100, 15), 3)
    Health_Bar=pygame.draw.rect(screen, health_color, (Health_Bar_Border.x, Health_Bar_Border.y, max(1, health), 15))
    screen.blit(HP_counter_text, (Health_Bar_Border.x+Health_Bar_Border.width+10, Health_Bar_Border.y))
    
    #Меню
    Menu_Border=pygame.draw.rect(screen, (255, 255, 255), (0, 275, 400, 400-275), 3)
    screen.blit(attack_button_text, (25, 285)) #вывожу текст атаки на экран
    attack_button=pygame.draw.rect(screen, (255, 255, 255), (25, 285, 50, 16), 1)


    if health >= 70:
        health_color = (0, 255, 0)
    elif health <70 and health > 40:
        health_color = (255, 255, 0)
    else:
        health_color = (255, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a and HP>0:
                HP-=5
            if event.key == K_b and HP<37:
                HP+=5
    pygame.display.update()
    clock.tick(60)
