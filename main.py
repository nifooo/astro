import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state



def main():
    class Player: 
        def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
            
            x = SCREEN_WIDTH / 2
            y = SCREEN_HEIGHT / 2



    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.draw(screen)
        screen.fill("black")
        pygame.display.flip()
     
        clock.tick(60)
        dt = clock.tick() / 1000
       # print(dt)


if __name__ == "__main__":
    main()
