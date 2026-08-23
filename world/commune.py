from random import randint, choice

from pygame.math import Vector2

from entities.house import House

from world.terrain import Terrain
from world.flood import Flood
from world.roads import Roads
from core.constants import NUM_HOUSES

from ai.hvi import HVI


class Commune:

    def __init__(self):

        self.terrain = Terrain(4000, 2500)

        self.flood = Flood()

        self.roads = Roads()

        self.houses = []

        for _ in range(NUM_HOUSES):

            road = choice(self.roads.roads)

            if road.width > road.height:
                # horizontal road
                x = randint(0, road.width)
                y = randint(-35, 35)

                wx = road.left + x
                wy = road.centery + y

            else:
                # vertical road
                x = randint(-35, 35)
                y = randint(0, road.height)

                wx = road.centerx + x
                wy = road.top + y

            house = House((wx, wy))

            # house.hvi = HVI.compute(house)

            self.houses.append(house)

    def update(self, dt):

        self.flood.update(dt)

        for house in self.houses:

            h = self.terrain.height(
                house.x,
                house.y,
            )

            house.flood_depth = self.flood.depth(h)
            
            if house.flood_depth > 0:

                house.wait_time += dt

                house.update_needs()

                if (
                    house.flood_depth > 0.2
                    or (
                        house.flood_depth > 0.04
                        and house.hvi > 0.325
                    )
                ):
                    house.emergency = True
                else:
                    house.emergency = False
                
            house.update_beacons()