
# range starts inclusive, exclusive, then step


def main():
    for i in range(2):
        print("Go, Cats, Go!")
        print("Go, Dogs, Go!")
    print("BEAR DOWN!")
    for i in range(3):
        print("Who's house?! COUGS HOUSE")

    for i in range(5):
        print(i)

    for num in range(2, 11, 2):
        print(num)

    a, b, c = 5, 0, -1
    for num in range(a, b, c):
        print(num)

    for line in range(1, 6):
        print("#" * line, end="")
        print("+" * (2 * line), end="")
        print("#" * line)

    for line in range(1, 6):
        print("#" * line, "+" * (2 * line), "#" * line, sep="")  # not the favorable way, above method better.

    for x in range(1, 6):
        for y in range(1, 10):
            print(y * x, end="\t")
        print()


main()
