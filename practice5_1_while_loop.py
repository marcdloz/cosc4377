import random


number = 1
while number <= 200:
    number *= 2
    print(number, end=" ")
print()


dividend = 21
divisor = 2
while dividend % divisor != 0:
    divisor += 1
print(divisor)


def main():
    print("This program picks numbers from 1 to 10")
    print("until a particular numbers comes up")

    num = int(input("Pick a number between 1 and 10? "))

    result = 0  # priming, set to 0 to make sure we enter the loop
    count = 0
    while result != num:
        result = random.randint(1, 10)
        print("next number = ", result)
        count += 1

    print("Your number came up after", count, "times")


main()
