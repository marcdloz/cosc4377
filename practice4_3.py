#   Computes n!, or the product of the integers 1 through n.
#   pre : n >= 0
import random


def factorial(n):
    if n < 0:
        raise ValueError("n must be greater or equal to 0")
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product


def abs_max(x, y):
    if abs(x) > abs(y):
        return x
    return y


def dice_roll(times):
    total = 0
    for i in range(times):
        die = random.randint(1, 6)
        print(die)

        if die == 1:
            return 0    # stop immediately
        else:
            total += die

    return total    # never rolled a 1


def main():
    """print(factorial(-1))"""
    max = abs_max(7, 5)
    print(max)
    total = dice_roll(5)
    print("total is:", total)


main()
