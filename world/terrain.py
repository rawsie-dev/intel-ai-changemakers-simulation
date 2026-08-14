from noise import pnoise2
import numpy as np


class Terrain:

    def __init__(self, width, height, scale=250):

        self.width = width
        self.height_pixels = height

        self.scale = scale

        self.heightmap = np.zeros(
            (height, width),
            dtype=np.float32,
        )

        self.generate()

    def generate(self):

        for y in range(self.height_pixels):

            for x in range(self.width):

                h = pnoise2(
                    x / self.scale,
                    y / self.scale,
                    octaves=5,
                    persistence=0.5,
                    lacunarity=2.0,
                    repeatx=999999,
                    repeaty=999999,
                    base=42,
                )

                self.heightmap[y, x] = h

        mn = self.heightmap.min()
        mx = self.heightmap.max()

        self.heightmap = (self.heightmap - mn) / (mx - mn)

    def height(self, x, y):

        x = max(0, min(self.width - 1, int(x)))
        y = max(0, min(self.height_pixels - 1, int(y)))

        return self.heightmap[y, x]