"""This file determines if ingredients are toxic or not"""


class Toxic:
    """Class represents toxins"""

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.toxins = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

    def make_alert_sound(self):
        """Returns string"""
        return "!!! \nThere is a toxin in the food! \n!!!! \nmade alert sound"

    def make_accept_sound(self):
        """Returns string"""
        return "*** \nToxin Free \n*** \nmade acceptance sound"

    def message(self):
        """Determines if ingredients are toxic or not"""
        for item in self.toxins:
            if item in self.ingredients:
                return self.make_alert_sound()
        return self.make_accept_sound()


test = Toxic('sodium nitrate').message()
print(test)
