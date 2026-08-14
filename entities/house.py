from random import random, randint
from entities.beacon import Beacon


class House:

    def __init__(self, pos):

        self.x, self.y = pos

        # Household

        self.people = randint(1, 6)

        self.stories = 1 if random() < 0.7 else 2

        self.elderly = randint(0, 2) if random() < 0.35 else 0

        self.children = randint(0, 2) if random() < 0.25 else 0

        self.disabled = random() < 0.08

        self.medical = random() < 0.06

        # AI

        self.hvi = 0.0

        self.priority = 0.0

        # Disaster state

        self.flood_depth = 0.0

        self.rescued = False

        self.alive = True

        self.wait_time = 0.0

        self.emergency = False

        self.beacon = Beacon()