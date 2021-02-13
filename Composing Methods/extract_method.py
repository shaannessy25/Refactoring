# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math


def user_input():
    """This method will return a list with a user input for each student"""
    grade_list = []
    number_of_student = 5
    for _ in number_of_student:
        grade_list.append(int(input('Enter a number: ')))
    return grade_list


def calculate_mean(grade_list):
    """Calculates the mean and standard deviation"""
    total = 0
    for grade in grade_list:
        total += grade
    mean = total / len(grade_list)
    sd = 0
    total_of_sqrs = 0
    for grade in grade_list:
        total_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(total_of_sqrs / len(grade_list))
    return mean, sd


def print_stat(mean, sd):
    """Gets input from user and returns a print statement"""
    user_input()
    calculate_mean()

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


user_input()
print_stat()
