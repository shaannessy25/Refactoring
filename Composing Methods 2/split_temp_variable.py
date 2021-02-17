"""This file prints the weight of sandwhich based on type"""


class Sandwhich:
    """Represents ingredients of a sandwhich"""

    def __init__(self, patty, pickle, tomatoes, buns):
        self.patty = patty
        self.pickle = pickle
        self.tomatoes = tomatoes
        self.buns = buns

    def ny_sandwhich(self, lettuce):
        """Returns the weight of New York sandwhich"""

        ny_sandwhich = (2 * self.patty + 4 * self.pickle + 3 * self.tomatoes + 2
                        * lettuce + 2 * self.buns)
        return print("NY Burger Weight", ny_sandwhich)

    def kimchi_sandwhich(self, mayo, golden_onion, kimchi):
        """Returns the weight of Kimchi sandwhich"""

        kimchi_sandwhich = (2 * self.patty + 4 * self.pickle + 3 * self.tomatoes
                            + kimchi + mayo + golden_onion + 2 * self.buns)
        return print("Seoul Kimchi Burger Weight", kimchi_sandwhich)


sandwhich_one = Sandwhich(70, 20, 15, 95).ny_sandwhich(25)
sandwhich_two = Sandwhich(70, 20, 15, 95).kimchi_sandwhich(5, 20, 30)
