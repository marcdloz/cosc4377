
# create a multi-dimensional list (first syntax)
temps = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

# create a multi-dimensional list (second syntax)
temps = [[0] * 5, [0] * 5, [0] * 5]

# get/set element values in a 2D list
print(temps[0][0])
temps[0][3] = 87    # set fourth value of first row
temps[2][0] = 99    # set first value of third row
print(temps[0][3])
print(temps[2][0])

print(len(temps))   # numbers of rows
print(len([0]))     # length of first row


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()


print_grid(temps)

# create a 3D list
outer = []
for i in range(4):
    # add a 2D list element to the outer 3D list
    inner = []
    for j in range(4):
        inner.append([0] * 4)
    outer.append(inner)
print(outer)


def fill_in(triangle):
    for i in range(len(triangle)):
        triangle[i] = [0] * (i + 1)
        triangle[i][0] = 1
        triangle[i][i] = 1
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]


def print_nice(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            print(triangle[i][j], end=" ")
        print()


def main():
    triangle = [0] * 11
    fill_in(triangle)
    print_nice(triangle)


main()
