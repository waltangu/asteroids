import pygame # type: ignore
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            random_angle = random.uniform(20,50)
            vector_a = self.velocity.rotate(random_angle)
            vector_b = self.velocity.rotate(-random_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = 1.2 * (vector_a)
            asteroid_b.velocity = 1.2 * (vector_b)
            self.kill()
                    