from pygame import Rect

from core.constants import (
    WORLD_WIDTH,
    WORLD_HEIGHT,
    ROAD_SPACING,
    ROAD_WIDTH,
)


class Roads:

    def __init__(self):

        self.roads = []

        self.generate()

    def generate(self):

        # Vertical roads

        x = ROAD_SPACING

        while x < WORLD_WIDTH:

            self.roads.append(
                Rect(
                    x - ROAD_WIDTH // 2,
                    0,
                    ROAD_WIDTH,
                    WORLD_HEIGHT,
                )
            )

            x += ROAD_SPACING

        # Horizontal roads

        y = ROAD_SPACING

        while y < WORLD_HEIGHT:

            self.roads.append(
                Rect(
                    0,
                    y - ROAD_WIDTH // 2,
                    WORLD_WIDTH,
                    ROAD_WIDTH,
                )
            )

            y += ROAD_SPACING