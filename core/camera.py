from pygame.math import Vector2

from core.constants import (
    WIDTH,
    HEIGHT,
    WORLD_WIDTH,
    WORLD_HEIGHT,
)


class Camera:

    def __init__(self):

        self.position = Vector2()

    def follow(self, target):

        self.position.x = target.x - WIDTH / 2
        self.position.y = target.y - HEIGHT / 2

        self.position.x = max(
            0,
            min(
                self.position.x,
                WORLD_WIDTH - WIDTH,
            ),
        )

        self.position.y = max(
            0,
            min(
                self.position.y,
                WORLD_HEIGHT - HEIGHT,
            ),
        )

    def world_to_screen(self, p):

        return Vector2(
            p.x - self.position.x,
            p.y - self.position.y,
        )