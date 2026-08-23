from pygame.math import Vector2

from core.constants import BOAT_SPEED


class Boat:
    def __init__(self, pos):
        self.position = Vector2(pos)
        self.target = None
        self.speed = BOAT_SPEED

    def update(self, dt):

        if self.target is None:
            return

        direction = self.target - self.position

        if direction.length() < 5:
            return

        direction.scale_to_length(self.speed * dt)

        self.position += direction