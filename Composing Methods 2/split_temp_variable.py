

class Sandwhich:
    def __init__(self, patty=None, pickle=None , tomatoes=None, 
                lettuce=None, buns=None, mayo=None, golden_onion=None, kimchi=None):
        self.patty = patty
        self.pickle = pickle
        self.tomatoes = tomatoes
        self.lettuce = lettuce
        self.buns = buns
        self.mayo = mayo
        self.golden_onion = golden_onion
        self.kimchi = kimchi
    def ny_sandwhich(self, patty, pickle, tomatoes, lettuce, buns):
        ny_sandwhich = (2 * patty + 4 * pickle + 3 * tomatoes + 2
                        * lettuce + 2 * buns)
        return print("NY Burger Weight", ny_sandwhich)

    def kimchi_sandwhich(self, patty, pickle, tomatoes, 
                        lettuce, buns, kimchi, mayo, golden_onion):
        kimchi_sandwhich = (2 * patty + 4 * pickle + 3 * tomatoes
                    + kimchi + mayo + golden_onion + 2 * buns)
        return print("Seoul Kimchi Burger Weight", kimchi_sandwhich)


sandwhich_one = Sandwhich().ny_sandwhich(70, 20, 25, 15, 95)
sandwhich_two = Sandwhich().kimchi_sandwhich(70, 20, 25, 15, 95, 30, 5, 20)


