class HVI:

    @staticmethod
    def compute(house):

        score = 0.0

        score += house.elderly * 0.18

        score += house.children * 0.08

        if house.disabled:
            score += 0.25

        # if house.medical:
        #     score += 0.30

        if house.stories == 1:
            score += 0.20

        score += house.people * 0.03

        return min(score, 1.0)