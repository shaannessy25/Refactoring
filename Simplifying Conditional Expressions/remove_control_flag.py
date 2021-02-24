"""This file returns items found in a list """


def find_food(food):
    """This function checks parameter to fridge list and returns a string"""

    fridge = ['onion', 'cucumber', 'Guacamole', 'kabob barg', 'wesabi']
    for item in fridge:
        if item in food:
            return f"Found: {food}"
    return "Not Found"


if __name__ == "__main__":
    FOOD_ITEM = 'wesabi'
    print(find_food(FOOD_ITEM))
