
"""This file uses a method to return a statement"""


def make_shirazi_salad(ingredients):
    """This method will check ingediants and print a statement"""
    food = ['cucumber', 'tomato', 'onion', 'lemon juice']
    for item in food:
        if item not in ingredients:
            print("lacks ingredients")
    print("Diced, mixed, and added salt to all ingredients")
    print('Your yummy shirazi salad is ready!')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
