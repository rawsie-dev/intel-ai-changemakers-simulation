from random import random, randint
from entities.beacon import Beacon


class House:
    def __init__(self, pos):
        self.x, self.y = pos

        # Household
        self.people = randint(1, 6)
        self.stories = 1 if random() < 0.7 else 2
        self.elderly = randint(0, min(2, self.people))

        remaining = self.people - self.elderly
        self.children = randint(0, min(2, remaining))

        self.disabled = random() < 0.08
        # Medical conditions
        # self.needs_medical = random() < 0.10
        # self.medical = random() < 0.03

        # Requests
        # request = random()

        # self.needs_food = request < 0.30
        # self.needs_clothes = 0.30 <= request < 0.45

        # Request progression
        self.food_need_time = random() * 20
        self.clothes_need_time = 20 + random() * 30
        self.medical_need_time = 50 + random() * 40

        self.needs_food = False
        self.needs_clothes = False
        self.needs_medical = False

        # AI
        self.hvi = 0.0
        self.priority = 0.0

        # Disaster state
        self.flood_depth = 0.0
        self.rescued = False
        self.alive = True
        self.wait_time = 0.0
        self.emergency = False

        # Beacons
        self.people_beacon = Beacon("PEOPLE")
        self.water_beacon = Beacon("WATER")
        self.request_beacon = Beacon("REQUEST")

    def update_beacons(self):

        self.people_beacon.update(self)
        self.water_beacon.update(self)
        self.request_beacon.update(self)

    def update_needs(self):

        if self.flood_depth <= 0:
            return

        # Food / water becomes necessary first
        if self.wait_time >= self.food_need_time:
            self.needs_food = True

        # Clothing becomes necessary later
        if self.wait_time >= self.clothes_need_time:
            self.needs_clothes = True

        # Medical assistance becomes necessary eventually
        if self.wait_time >= self.medical_need_time:
            self.needs_medical = True