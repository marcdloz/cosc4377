# Can create list of fixed size by list = [None] * 10,
# elements still empty but now fixed size.

odd_integer = 0
odds_list = []
for i in range(-6, 38):
    if abs(i) % 2 == 1:
        odds_list.append(i)
        odd_integer += 1
print(odds_list)
