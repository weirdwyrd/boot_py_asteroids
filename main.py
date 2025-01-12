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


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # game engine
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # background
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # characters
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:  # game loop
        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # draw screen
        pygame.Surface.fill(screen, (0, 0, 0))
        # draw characters
        player.draw(screen)
        # render
        pygame.display.flip()

        # clock
        dt = clock.tick(60) / 1000  # divide to get ms from sec


# main


if __name__ == "__main__":
    main()
