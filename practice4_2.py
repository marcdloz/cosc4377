

def print_hailstone_max_min(start, length):
    min, max = start, start
    print(start, end=" ")

    value = start
    for i in range(length - 1):
        if value % 2 == 0:
            value = value // 2
        else:
            value = 3 * value + 1
        print(value, end=" ")

        if value > max:
            max = value
        elif value < min:
            min = value

    print()
    print("max = ", max)
    print("min = ", min)


def main():

    how_many = int(input("How many numbers do you have? "))

    negatives, sum, product = 0, 0, 1
    for i in range(how_many):
        next = float(input("Next number? "))
        sum += next
        product *= next
        if next < 0:
            negatives += 1

    print()
    if how_many <= 0:
        print("No numbers to average")
    else:
        average = sum / how_many
        print("average =", average)

    print("sum =", sum, "and product =", product)
    print("# of negatives =", negatives)
    """print_hailstone_max_min(7, 10)"""

    dollars1 = 0.01 + 0.05 + 0.10 + 0.25
    dollars2 = 0.25 + 0.10 + 0.05 + 0.01

    if dollars1 == dollars2:
        print("True")
    else:
        print("False")

    if abs(dollars1 - dollars2) < 0.001:    # can use math.isclose() instead
        print("True")
    else:
        print("False")


main()
