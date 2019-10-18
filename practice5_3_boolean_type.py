
# defining a boolean variable
x, number = 2, 20
even = (number % 2 == 0)
print(even)

if number >= 1 and even:
    print("OK!")

if x in [1, 2, 3]:
    print("YES!")

# code with a boolean variable
positive = (number > 0)
if positive:
    print("number is positive")
else:
    print("number is not positive")

name = "Evelyn"
print(name.endswith("n"))
if name.startswith("Eve"):
    print("What a cute lion cub!")

# improved negative boolean test
name = "Larry"
if not name.startswith("Eve"):
    print("I am not Eve!")

# improved "zen" implementation
n = 55
print(10 >= n <= 99) and (n % 10 != n / 10)


def first_word(s):
    start = 0
    while start < len(s) and s[start] == " ":
        start += 1
    stop = start
    while stop < len(s) and s[stop] != " ":
        stop += 1
    return s[start:stop]


def is_prime(z):
    for i in range(2, n):
        if z % i == 0:
            return False
    return True


print(is_prime(11))
print(first_word(" worlds"))

