
def average_of_values(values):
    average = 0
    count = 0
    for value in values:
        average += value
        count += 1
    return average / count


list = {1, -2, 4, -4, 9, -6, 16, -8, 25, -10}
mean = average_of_values(list)
print(mean)
