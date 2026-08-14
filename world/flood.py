class Flood:

    def __init__(self):

        self.level = 0.05

        self.rise_rate = 0.0125

    def update(self, dt):

        self.level += self.rise_rate * dt

        self.level = min(self.level, 1.0)

    def depth(self, terrain_height):

        return max(0.0, self.level - terrain_height)