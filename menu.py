import pygame, my_sprites, main
from pygame.locals import *
m=main


health_font=pygame.font.SysFont('Engravers MT', 10)
menu_font=pygame.font.SysFont('Engravers MT', 14)

attack_button_text=menu_font.render(('attack'), True, (255, 255, 255))
heal_button_text=menu_font.render(('heal'), True, (255, 255, 255))

def menu(m1_down):
    attack=False
    heal=False
    pygame.draw.rect(m.screen, (0, 0, 0), (0, 240, m.WIDTH, m.HEIGHT-240))
    pygame.draw.rect(m.screen, (255, 255, 255), (0, 240, m.WIDTH, m.HEIGHT-240), 2)
    m.screen.blit(attack_button_text, (17, 302)) #кнопка атаки
    attack_button=pygame.Rect(15, 300, attack_button_text.get_width()+4, 14)
    pygame.draw.rect(m.screen, (255, 255, 255), attack_button, 2)
    m.screen.blit(heal_button_text, (17, 332))
    heal_button=pygame.Rect(attack_button.x, attack_button.y+30, heal_button_text.get_width()+4, attack_button.height)
    pygame.draw.rect(m.screen, (255, 255, 255), heal_button, 2)

    press=m1_down
    if attack_button.collidepoint(pygame.mouse.get_pos()) and press == True:
        attack=True
        
    if heal_button.collidepoint(pygame.mouse.get_pos()) and press == True:
        heal=True
    return attack, heal
    