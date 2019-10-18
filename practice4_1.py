import math


current_score = 1000
max_score = 500
number, answer = 9, 0

if current_score > max_score:
    print("A new high score!")
    max_score = current_score

if number >= 0:
    answer = math.sqrt(number)
    print(answer)
else:
    answer = -1
    print(answer)

print(2 + 2 == 4)
print(4 < 3)

print(2 < 2.5)
print(int("40") > 35)   # Convert string to integer and compare
print("42" == 42)   # Compare == between string and integer
"""print("42" > 40)    # Compare > between string and integer, results in TypeError"""

if number > 0:
    print("Number is positive")
if number == 0:
    print("Number is zero.")
if number < 0:
    print("Number is negative")


if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero.")
else:
    print("Number is negative")


money = 2000
print("You have $", money, "left")

if money < 500:
    print("Cash is dangerously low. Bet carefully")
elif money < 1000:
    print("Cash is somewhat low. Bet moderately")
else:
    print("Cash is in good shape. Bet liberally")

bet = int(input("How much do you want to bet? "))


age1 = 20
age2 = 16
if age1 >= 18 > age2:
    print("OK!")




