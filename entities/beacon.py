class Beacon:

    PEOPLE_STATES = (
        "GREEN",
        "BLUE",
        "RED",
    )

    WATER_STATES = (
        "WHITE",
        "GREEN",
        "BLUE",
        "RED",
    )

    REQUEST_STATES = (
        "WHITE",
        "CYAN",
        "YELLOW",
        "MAGENTA",
    )

    def __init__(self, beacon_type):

        self.type = beacon_type

        if beacon_type == "WATER":
            self.state = "WHITE"

        elif beacon_type == "REQUEST":
            self.state = "WHITE"

        else:
            self.state = "GREEN"

    def update(self, house):

        if self.type == "PEOPLE":
            self.update_people(house)

        elif self.type == "WATER":
            self.update_water(house)

        elif self.type == "REQUEST":
            self.update_request(house)

    def update_people(self, house):

        if house.people <= 2:
            self.state = "GREEN"

        elif house.people <= 4:
            self.state = "BLUE"

        else:
            self.state = "RED"

    def update_water(self, house):

        depth = house.flood_depth

        # No water
        if depth <= 0:
            self.state = "WHITE"

        # Low water
        elif depth < 0.25:
            self.state = "GREEN"

        # Moderate water
        elif depth < 0.5:
            self.state = "BLUE"

        # High water
        else:
            self.state = "RED"

    def update_request(self, house):

        if house.flood_depth <= 0:
            self.state = "WHITE"
            return

        if house.needs_medical:
            self.state = "MAGENTA"

        elif house.needs_clothes:
            self.state = "YELLOW"

        elif house.needs_food:
            self.state = "CYAN"

        else:
            self.state = "WHITE"

    def is_on(self, time):

        # All states are illuminated,
        # except MAGENTA which blinks.
        if self.state == "MAGENTA":
            return ((time*4) % 1.0) < 0.5

        return True