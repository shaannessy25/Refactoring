"""Methods for various calculations"""


def area_under_graph(graph):
    """Calculate the area under the input graph."""
    # Still working
    return graph


def get_max_value(num_list):
    """This method finds the max value in a list"""
    max_value = num_list[0]
    for value in num_list:
        max_value = value if value > max_value else max_value
    return max_value


li = [5, -1, 43, 32, 87, -100]
print(get_max_value(li))


def split_string(sentence):
    """This method splits the words in a sentence"""
    words = sentence[0:].split(' ')
    return words


print(split_string('If you were a vegetable, you’d be a ‘cute-cumber.'))
