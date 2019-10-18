import math
import random
import time


def sum_of(n):
    return (n + 1) * n // 2     # Floor division


def quadratic(a, b, c):
    disc = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + disc) / (2 * a)
    root2 = (-b - disc) / (2 * a)
    return root1, root2


def main():
    x = 3.647
    y = round(x)
    z = 1
    print(y)
    print("nearest integer is", round(x, 1))
    print("nearest integer is", round(x, 2))
    for i in range(1, 6):
        root = math.sqrt(i)
        print("square root of", i, "is", int(round(root, 2)))

    for i in range(1, 6):
        z *= i
    print(z)

    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    r3 = random.randint(1, 10)
    print("Three random numbers:", r1, r2, r3)

    random.randrange(-1, 2, 2)  # -1, 0, 1, 2, but only -1 and 1 can be picked since it is by every 2.

    """STEPS = 20
    position = 10

    for i in range(STEPS):
        # pause for 200ms
        time.sleep(0.2)

        # randomly adjust position by -1 or +1
        rnd = random.randrange(-1, 2, 2)
        position += rnd

        # print character as its current.position
        print(" " * position, "*")"""

    answer = sum_of(100)
    print("sum of 1-100 is", answer)

    r1, r2 = quadratic(2, 6, 4)
    print("The roots are", r1, "and", r2)

    r1, r2 = quadratic(1, -5, 6)
    print("The roots are", r1, "and", r2)


main()
