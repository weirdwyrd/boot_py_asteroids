import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2
        )

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # no splitting
        random_angle = random.uniform(20, 50)
        left_dir = pygame.Vector2.rotate(self.velocity, random_angle)
        right_dir = pygame.Vector2.rotate(self.velocity, random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left = Asteroid(self.position.x, self.position.y, new_radius)
        left.velocity = left_dir * (1 + random_angle * 0.01)
        right = Asteroid(self.position.x, self.position.y, new_radius)
        right.velocity = right_dir * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
