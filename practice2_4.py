# This program draws two triangular figures using loops.

LINES = 3


def downward_triangle():
    for line in range(1, LINES + 1):
        print(" " * (line - 1), end="")
        print("*" * (2 * LINES + 1 - 2 * line))


def upward_triangle():
    for line in range(LINES, 0, -1):
        print(" " * (line - 1), end="")
        print("*" * (2 * LINES + 1 - 2 * line))


def main():
    downward_triangle()
    print()
    upward_triangle()


main()
