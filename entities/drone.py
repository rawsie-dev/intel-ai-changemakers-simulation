from pygame.math import Vector2
from core.constants import (WORLD_WIDTH, DRONE_SPEED)

class Drone:

    def __init__(self):

        self.position = Vector2(300, 300)

        self.direction = Vector2(1, 0)

        self.speed = DRONE_SPEED

    def update(self, dt):

        self.position += self.direction * self.speed * dt

        if self.position.x > WORLD_WIDTH:
            self.position.x = 0