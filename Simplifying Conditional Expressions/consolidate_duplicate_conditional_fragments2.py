"""This file takes returns a statement based on initial values"""


class Gear:
    """Class represents car gears"""

    def __init__(self, speed, gear=1):
        self.speed = speed
        self.gear = gear

    def change_gear(self):
        """Returns a string"""
        return f"Gear changed to: {self.gear}"

    def display_gear(self):
        """Returns a string"""
        return f"Displayed gear: {self.gear}"

    def process_speed(self):
        """This method checks speed, then updates and displays gears"""
        if self.speed >= 0 or self.speed < 30:
            self.gear = 1
        elif self.speed >= 30 or self.speed < 50:
            self.gear = 2
        elif self.speed >= 50 or self.speed <= 90:
            self.gear = 3
        elif self.speed >= 90:
            self.gear = 4
        elif self.speed <= 0:
            self.gear = 'R'
        return f"{self.change_gear()} \n{self.display_gear()}"


car_speed = Gear(-5).process_speed()
print(car_speed)
