import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        # Checks for collision with another circle shape
        return pygame.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius)
    
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

        self.velocity = pygame.Vector2(0, 1)
        self.rotation = rotate(self.rotation)
        
    def draw(self, screen):
        pygame.draw.circle(surface= screen, color= "white", center= self.position, radius= self.radius, width= 2)

    def update(self, dt):
        self.position += (self.velocity * dt)