
"""This file determines if a person is above the drinking age and
    can enter a nightclub"""
LEGAL_DRINKING_AGE = 21


class Person:
    """Represents a person"""

    def __init__(self, age):
        self.age = age

    def enter_night_club(self):
        """This method determines if you can enter a night club"""
        if self.age >= LEGAL_DRINKING_AGE:
            print("Allowed to enter.")
        else:
            print("Enterance of minors is denited.")

    def older_than_18_year_old(self):
        """This method determines if the person is older than 18"""
        if self.age >= LEGAL_DRINKING_AGE:
            return True
        return False


person = Person(17.9)
person.enter_night_club()
