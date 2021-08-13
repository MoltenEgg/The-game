import pygame
import sys
import my_sprites
import pygame.locals


pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption("The best game")
SIZE=WIDTH, HEIGHT=640, 480
screen=pygame.display.set_mode(SIZE)


FPS=60
ENEMY_PLACEMENT=ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y=(40, 40)
Hp=37 #тестовое значение здоровья
HpMAX=Hp


def drawing():
    screen.fill((0, 0, 0)) 
    health_bar=pygame.draw.rect(screen, (0, 255, 0), (ENEMY_PLACEMENT_x, ENEMY_PLACEMENT_y+66, Hp, 5))
    screen.blit(my_sprites.goblin, (ENEMY_PLACEMENT))

def main():
    RUN=True
    while RUN:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
        drawing()        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
