import pygame # type: ignore
from constants import *
from asteroidfield import *
from player import Player
from asteroid import Asteroid
from bullet import Bullet

def main():
    pygame.init()
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Player.containers = updatable, drawable
    Bullet.containers = shots, updatable, drawable
    player = Player(x,y)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for u in updatable:
            u.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!")
                return 
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000
       
if __name__ == "__main__":
    main()