
# define some tuples
pt = (34, 7)
date = (2019, 12, 25)

# interact with tuples: indexing, concatenation
print(pt)
print(pt[0])
print(pt + date)
print(len(date))
print(date[1:3])

# zero and one element tuples
empty_tuple = ()
one_element = (42,)

# convert between tuple and list
xmas = (12, 25)
xmas_list = list(xmas)
print(xmas_list)
xmas_list.append(2019)
print(xmas_list)
xmas = tuple(xmas_list)
print(xmas)

# unpack a tuple
year, month, day = date
print(year, month, day)

# swap integers using unpacking assignment statement
a, b = 35, 17
(a, b) = (b, a)
print(a, b)

# demonstrate the enumerate function
pets = ["Abby", "Barney", "Clyde", "Mandy", "Rajah"]
print(list(enumerate(pets)))
for i, name in enumerate(pets): # can get both i and element this way
    print("element", i, "is", name)

# demonstrate the zip function
firsts = ["Allison", "Marty", "Stuart"]
lasts = ["Obourn", "Stepp", "Reges"]
print(list(zip(lasts, firsts)))
for last, first in zip(lasts, firsts):
    print("last name is", last, "and first name is", first)

for i, (last, first) in enumerate(zip(lasts, firsts)):
    print(i, first, last)

