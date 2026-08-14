class Beacon:

    STATES = (
        "GREEN",
        "YELLOW",
        "RED",
        "WHITE",
    )

    def __init__(self):

        self.state = "GREEN"

    def update(self, house):

        if house.rescued:
            self.state = "GREEN"
            return

        if house.emergency:

            if house.medical or house.flood_depth > 0.8:
                self.state = "RED"
            else:
                self.state = "YELLOW"

        else:

            self.state = "GREEN"

    def is_on(self, time):

        t = time % 1.0

        if self.state == "GREEN":
            return True

        if self.state == "YELLOW":
            return t < 0.5

        if self.state == "RED":
            return (time * 4) % 1 < 0.5

        if self.state == "WHITE":
            return (
                t < 0.15
                or 0.3 < t < 0.45
            )

        return False