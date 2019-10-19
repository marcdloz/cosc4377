
def max_value(values):
    max_number = -99999
    for value in values:
        if value > max_number:
            max_number = value
    return max_number


list = {12, 7, -1, 25, 3, 9}
max = max_value(list)
print(max)
