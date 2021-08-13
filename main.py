import pygame
import sys
import my_sprites

pygame.init()

SIZE=WIDTH, HEIGHT=640, 480
FPS=60
Clock=pygame.time.Clock
pygame.display.set_caption("The best game")

screen=pygame.display.set_mode(SIZE)

def drawing():
    screen.fill((0, 0, 0)) 
    
    screen.blit(my_sprites.goblin, (40, 40))
def main():
    RUN=True
    while RUN:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                RUN=False
                sys.exit()
        drawing()        
        pygame.display.update()
        Clock.tick(FPS) #проверить TAB

if __name__ == '__main__':
    main()
