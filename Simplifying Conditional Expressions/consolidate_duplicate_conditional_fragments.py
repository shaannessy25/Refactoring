"""This file returns ingredients of a drink"""


class Drink:
    """Represents a standard drink"""

    def __init__(self, drink, addons):
        self.drink = drink
        self.addons = addons
        self.mix = []

    def add(self, ingredient):
        """Adds ingredients to mix list"""
        return self.mix.append(ingredient)

    def mixer_ice_with_cream(self):
        """Adds ice cream to list returns statement"""
        self.add('ice')
        self.add('cream')
        return print('mixed with ice cream')

    def make_drink(self):
        """Method returns list of ingredients"""
        if 'coffee' in self.drink:
            self.add('coffee')
            self.add(self.addons)
        if 'strawberry milkshake' in self.drink:
            self.mixer_ice_with_cream()
            self.add('strawberry')
            self.add(self.addons)
        return self.mix


milkshake = Drink('strawberry milkshake', ['milk', 'sugar']).make_drink()

print(milkshake)
