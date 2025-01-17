import sys
import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MAX_RADIUS,
)
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game engine
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # grouping
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    # characters
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    # delta
    dt = 0

    while True:  # game loop
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if player.check_collision(a):
                sys.exit("Game over!")
            for s in shots:
                if s.check_collision(a):
                    s.kill()
                    a.split()

        # draw screen
        pygame.Surface.fill(screen, (0, 0, 0))

        # draw characters
        # player.update(dt)
        # player.draw(screen)

        for d in drawable:
            d.draw(screen)

        # render
        pygame.display.flip()

        # clock
        dt = clock.tick(60) / 1000  # divide to get ms from sec


# main


if __name__ == "__main__":
    main()
