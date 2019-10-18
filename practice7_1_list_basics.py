
# making a list from a range of integers
mylist = list(range(1, 11))
print(mylist)

# using * operator to create list of a given length
temperature = [0.0] * 3
print(temperature)

# get a list from a string or file
words = "to be or not to be".split()
print(words)

# accessing elements by index
temperature2 = [94, 90, 87, 35, 62]
print(temperature2[0])
print(temperature2[1 + 1])
print(temperature2[4])

# modifying elements by index
temperature2[2 + 2] = 25 + 25
print(temperature2[4])

# works for a list of any length
print("first =", temperature2[0])
print("middle =", temperature2[len(temperature2) // 2])
print("last =", temperature2[-1])

# things you can do to an integer element of a list
i = 2
temperature2[i] = 3
temperature2[i] += 1
temperature2[i] *= 2
temperature2[i] -= 1
print(temperature2[i])

# slicing a list
nums = [10, 20, 30, 40, 50, 60, 70, 80]
print(nums[2:4])
print(nums[:4])
print(nums[4:])
print(nums[1:7:2])
print(nums[1::2])
print(nums[5:1:-1])
print(nums[::-1])

# for loop over list elements, can't modify list this way. (for-each loop)
for temp in temperature2:
    print(temp)

# for loop to modify elements by index
for i in range(len(temperature2)):
    temperature2[i] += 1
print(temperature2)

# read values from user input into a list
"""temperature3 = [0] * 5
for i in range(len(temperature3)):
    temperature3[i] = int(input("Type a number: "))
print(temperature3)"""

# adding element to end of list with append
data = []
print(len(data))
data.append("tool")
print(data)
data.append("time")
print(data)
print(len(data))

# adding element to a list with insert
data.insert(1, "Tim")
print(data)

# removing elements from a list by index, dynamically shifts so be aware
del data[0]
del data[1]
print(data)
element = data.pop(0)   # pop method does removes element at returns
print(element)

# removing elements from a list by value
data.append('Tim')
data.append('Allen')
data.remove('Tim')
print(data)

# clear the elements from a list
data.clear()
print(data)

# use + operator and extend method
data1 = [1, 2, 3]
data2 = [4, 5]
data3 = data1 + data2
print(data3)
data2.extend([6, 7])
print(data2)

# demonstrates global list functions
print(min(data3))
print(max(data3))
print(sum(data3))






