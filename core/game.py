import pygame

from pygame.math import Vector2

from world.commune import Commune
from entities.boat import Boat
from entities.drone import Drone
from core.camera import Camera


def lerp(a, b, t):
    return tuple(
        int(x + (y - x) * t)
        for x, y in zip(a, b)
    )


class Game:

    def __init__(self):

        self.commune = Commune()

        self.camera = Camera()

        self.boat = Boat((250, 250))

        self.drone = Drone()
        
        self.time = 0

    def update(self, dt):
        self.time += dt

        self.boat.update(dt)

        self.drone.update(dt)
        
        self.commune.update(dt)
        
        self.camera.follow(self.drone.position)

    def draw(self, screen):

        screen.fill((225, 235, 210))

        terrain = self.commune.terrain
        flood = self.commune.flood
        
        STEP = 8

        for y in range(0, terrain.height_pixels, STEP):

            for x in range(0, terrain.width, STEP):

                screen_x = x - self.camera.position.x
                screen_y = y - self.camera.position.y

                if (
                    screen_x < -STEP
                    or screen_x > 1600
                    or screen_y < -STEP
                    or screen_y > 900
                ):
                    continue

                height = terrain.height(x, y)

                depth = flood.depth(height)

                if depth > 0:

                    blue = min(255, int(120 + depth * 400))

                    color = (60, 120, blue)

                else:

                    g = int(90 + height * 165)

                    color = (70 + height * 160, g, 70 + height * 160)

                pygame.draw.rect(
                    screen,
                    color,
                    (screen_x, screen_y, STEP, STEP),
                )
                
        for road in self.commune.roads.roads:

            r = road.move(
                -self.camera.position.x,
                -self.camera.position.y,
            )
            
            pygame.draw.rect(
                screen,
                (150, 150, 150),
                r.inflate(4, 4),
            )

            pygame.draw.rect(
                screen,
                (80, 80, 80),
                r,
            )

        for house in self.commune.houses:

            p = self.camera.world_to_screen(
                Vector2(house.x, house.y)
            )
            
            if house.emergency:

                color = (255, 40, 40)

            elif house.flood_depth > 0:

                color = (255, 180, 0)

            else:

                color = (40, 180, 40)

            pygame.draw.circle(
                screen,
                (120, 120, 120),
                p,
                6,
            )
            
            if house.beacon.is_on(self.time):

                colors = {
                    "GREEN": (40, 255, 40),
                    "YELLOW": (255, 220, 40),
                    "RED": (255, 50, 50),
                    "WHITE": (255, 255, 255),
                }

                pygame.draw.circle(
                    screen,
                    colors[house.beacon.state],
                    (int(p.x), int(p.y - 10)),
                    3,
                )

        boat_pos = self.camera.world_to_screen(
            self.boat.position
        )

        pygame.draw.circle(
            screen,
            (20, 120, 255),
            boat_pos,
            8,
        )

        drone_pos = self.camera.world_to_screen(
            self.drone.position
        )

        pygame.draw.circle(
            screen,
            (255, 50, 255),
            drone_pos,
            5,
        )
        
        font = pygame.font.SysFont(None, 26)

        legend = [
            ("RED", (255, 50, 50)),
            ("YELLOW", (255, 220, 40)),
            ("GREEN", (40, 255, 40)),
        ]

        for i, (name, color) in enumerate(legend):

            y = 20 + i * 30

            pygame.draw.circle(screen, color, (20, y), 6)

            screen.blit(
                font.render(name, True, (0, 0, 0)),
                (35, y - 8),
            )
        
        screen.blit(font.render(f"Flood Level: {self.commune.flood.level:.2f}", True, (0, 0, 0)), (20, 120))