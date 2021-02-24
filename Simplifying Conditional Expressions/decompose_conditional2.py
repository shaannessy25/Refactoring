"""This file determines health based on chlostrol"""


def get_cholostrol(total_cholostrol, ldl, triglyceride):
    """This function checks inputs and returns a string"""

    if total_cholostrol < 200 and ldl < 100 and triglyceride < 150:
        return "*** Good level of cholestrol ***"

    elif 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200:
        # High cholestrol level
        return "*** High cholestrol level *** \nstart taking pills such as statins \nstart TlC diet"

    else:
        return "*** Borderline to moderately elevated ***\nStart TLC diet"\
            "\nUnder this meal plan, only 7 percent of your daily calories"\
            "\nshould come from saturated fat. Some foods help your"\
            "digestive tract absorb less cholesterol. For example,"\
            "\nyour doctor may encourage you to eat more: oats, barley,"\
            "and other whole grains. \nfruits such as apples, pears,"\
            "bananas, and oranges."

    return 'Error: unhandled case.'


print(get_cholostrol(220, 150, 180))
