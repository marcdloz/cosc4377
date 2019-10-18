# Prints a box filled with dots using a size parameter.


"""def draw_box(size):
    print("*" * size)
    for line in range(size - 2):
        print("*", "." * (size - 2), "*", sep="")
    print("*" * size)"""


def draw_box(width = 8, height = 4):
    print("*" * width)
    for line in range(height - 2):
        print("*", "." * (width - 2), "*", sep="")
    print("*" * width)


def main():
    """draw_box(size = 4)  # Can do size = 5 to be more explicit or simply 5 works."""
    draw_box(10, 5)
    draw_box()  # Utilizing optional parameters, can combine with required parameters.


main()
