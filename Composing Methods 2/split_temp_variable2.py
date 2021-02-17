"""This application prints age of user based on inputs"""


def age_finder():
    """This method will calculate and print the users age"""
    username = input('Please enter your username: ')
    current_year = input('Please enter current year: ')
    age_input = int(input('Please enter your birth year: '))
    age = current_year - age_input
    return print(f"Hi {username}! you are,{age} years old.")


if __name__ == '__main__':
    age_finder()
